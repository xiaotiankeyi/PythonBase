#!/usr/bin/env python

import pika
import logging


class RabbitMQClient:
    def __init__(self):
        self.exchange_type = "topic"  # 特定的路由键完全匹配,会推送到指定的队列上
        self.credentials = pika.PlainCredentials('admin', 'admin')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='192.168.0.121', port=5672, credentials=self.credentials))
        self.channel = self.connection.channel()
        self._declare_retry_queue()
        logging.debug("Rabbitmq队列连接成功")

    def _declare_retry_queue(self):
        """
        创建异常交换器和队列,用于存放没有正常处理的消息。
        :return:
        """
        self.channel.exchange_declare(exchange='RetryExchange',
                                      exchange_type='fanout',
                                      durable=True)
        self.channel.queue_declare(queue='RetryQueue',
                                   durable=True)
        # 绑定队列到指定的交换机
        self.channel.queue_bind('RetryQueue', 'RetryExchange', 'RetryQueue')

    # 生成交换机,返回交换机对象
    def declare_exchange(
            self,
            exchange=None,  # 交换机的名字,为空则自动创建一个名字
            exchange_type='',  # 默认交换机类型为direct
            passive=False,  # 检查交换机是否存在,存在返回状态信息,不存在返回404错误
            durable=False,  # 设置是否持久化）
            auto_delete=False,  # 最后一个队列解绑则删除
            internal=False,  # 是否设置为值接收从其他交换机发送过来的消息,不接收生产者的消息
            arguments=None):  # 一个字典,用于传递额外的参数

        self.channel.exchange_declare(exchange=exchange,
                                      exchange_type=exchange_type if exchange_type else self.exchange_type,
                                      durable=True)

    # 生成队列,返回队列对象
    def declare_queue(
            self,
            queue='',  # 队列的名字,默认为空,此时将自动创建一个名字,
            passive=False,  # 检查一下队列是否存在,如果该参数为True,该方法判断队列存在否,不会声明队列；存在返回queue的状态,不存在报错
            durable=False,  # 队列持久化参数,默认不持久化
            exclusive=False,  # 设置独享队列,该队列只被当前的connection使用,如果该tcp关闭了,队列会被删除
            auto_delete=False,  # 当最后一个消费者退订后自动删除,默认不开启
            arguments=None):  # 一个字典,用于队列传递额外的参数
        self.channel.queue_declare(queue=queue,
                                   durable=True)

    def declare_delay_queue(self, queue, durable=True, DLX='RetryExchange', TTL=""):
        """
        创建延迟队列
        :param TTL: ttl的单位是us,ttl=60000 表示 60s
        :param queue:
        :param DLX:死信转发的exchange
        :return:
        """
        arguments = {}
        if DLX:
            # 设置死信转发的exchange,延迟结束后指向的交换机(死信收容交换机)
            arguments['x-dead-letter-exchange'] = DLX
        if TTL:
            # 消息的存活时间,消息过期后会被指向(死信收容交换机)收入死信队列
            arguments['x-message-ttl'] = TTL
        print('额外信息:', arguments)
        self.channel.queue_declare(queue=queue,  # 声明队列
                                   durable=durable,  # 持久化
                                   arguments=arguments)

    def bind_queue(
            self,
            queue,  # 队列的名字
            exchange,  # 交换机的名字
            routing_key=None,  # 路由键规则,当为None时,默认使用queue的名字作为路由键规则
            arguments=None):  # 一个字典,传递额外的参数
        self.channel.queue_bind(queue=queue,
                                exchange=exchange,
                                routing_key=routing_key,
                                )
        # 返回绑定队列的状态信息

    def bind_exchange(
            self,
            destination=None,  # 目的交换机的名字
            source=None,  # 源交换机的名字
            routing_key='',  # 路由键规则,当为None时,默认使用queue的名字作为路由键规则
            arguments=None):  # 一个字典,传递额外的参数
        self.channel.exchange_bind(destination=destination,
                                   source=source)
        # 返回绑定交换机的状态信息

    # 定义成产者生产消息
    def basic_publish(
            self,
            exchange,  # 交换机的名字
            routing_key,  # 路由键,topic交换机是扇形交换机,可以随便写
            body,  # 消息主体
            properties=None,  # 消息的属性
            mandatory=False,  # 是否设置消息托管
            immediate=False):  # 是否消息实时同步确认,一般和confirm模式配合使用
        self.channel.basic_publish(exchange=exchange,
                                   routing_key=routing_key,
                                   body=body,
                                   properties=pika.BasicProperties(
                                       delivery_mode=2,
                                       type=exchange
                                   ))
        print("生产者推送消息成功")

    def __publish_init__(
            self, content_type=None, content_encoding=None, headers=None, delivery_mode=None,
            priority=None,
            correlation_id=None, reply_to=None, expiration=None, message_id=None, timestamp=None,
            type=None,
            user_id=None, app_id=None, cluster_id=None):
        self.content_type = content_type  # 消息的类型,如text/html,json等
        self.content_encoding = content_encoding  # 消息的编码,如gbk,utf-8等
        self.headers = headers  # 消息头,可以和头交换机约定规则
        self.delivery_mode = delivery_mode  # 消息持久化,2表示持久化,
        self.priority = priority  # 消息的优先权
        self.correlation_id = correlation_id
        self.reply_to = reply_to
        self.expiration = expiration  # 消息的有效期
        self.message_id = message_id  # 消息iD,自动管理
        self.timestamp = timestamp  # 消息的时间戳
        self.type = type
        self.user_id = user_id
        self.app_id = app_id  # 发布应用的ID
        self.cluster_id = cluster_id

    def basic_consume(
            self,  # 启动队列消费者,告诉服务端开启一个消费者
            consumer_callback,  # 消费者回调函数
            queue,  # 队列名称
            auto_ack=False,  # 发送确认,默认开启消息确认模式,为True是关闭消息确认；如果回调函数中不发送消息确认,消息会一直存在队列中,等待推送给新连接的消费者
            exclusive=False,  # 设置独享消费者,不允许其他消费者订阅该队列
            consumer_tag=None,  # 消费者标签,如果不指定,系统自动生成
            arguments=None):  # 字典,额外的参数
        print("消费者开始消费消息")
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(
            on_message_callback=consumer_callback,
            queue=queue,
            auto_ack=auto_ack
        )

    # 接收消息处理函数,回调函数
    def callback_success(
            self,
            channel,  # 信道
            method,  # 一个交付的deliver对象,用来通知客户端消息
            properties,  # 消息的属性,就是消息在发送时定义的属性
            body):  # 消息的主题,二进制格式
        print(str(body.decode('utf-8')))
        print('接收成功！')
        # 发送确认
        channel.basic_ack(delivery_tag=method.delivery_tag)
        print('回复确认消息')

    # 失败函数,将消息重新放回队列中
    def callback_failed(
            self,
            channel,  # 信道
            method,  # 一个交付的deliver对象,用来通知客户端消息
            properties,  # 消息的属性,就是消息在发送时定义的属性
            body):  # 消息的主题,二进制格式
        print(str(body.decode('utf-8')))
        print('接收失败！')
        channel.basic_nack(delivery_tag=method.delivery_tag, requeue=True)
        print('将当前消息重新放入队列中')

    # 失败函数,将消息重新放回队列中
    def callback_reject(
            self,
            channel,  # 信道
            method,  # 一个交付的deliver对象,用来通知客户端消息
            properties,  # 消息的属性,就是消息在发送时定义的属性
            body):  # 消息的主题,二进制格式
        print(str(body.decode('utf-8')))
        print('接收失败！')
        channel.basic_reject(delivery_tag=method.delivery_tag, requeue=False)

    def close_channel(self):
        self.connection.close()

    def start_consuming(self):
        self.channel.start_consuming()
