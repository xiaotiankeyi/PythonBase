import pika
import base64
import time
from pika import exceptions

credentials = pika.PlainCredentials('admin', 'admin')
# 1、连接rabbitmq服务器连接
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.0.121', port=5672, credentials=credentials))
# 如果并发量较高，可以将connection作为单例返回过去，不用频繁的连接

# 建立管道
channel = connection.channel()

# 2、创建一个名为hello的队列,需要和消费者队列保持一致
# channel.queue_declare(queue='hello', durable=False,
#                       exclusive=False, auto_delete=False,
#                       arguments={
#                           "x-message-ttl": 60000    # 队列存活时间
#                       })

# 开启确认机制标志
channel.confirm_delivery()
try:
    channel.basic_publish(exchange='',      # exchange指定交换机
                          routing_key='hello',
                          body='我真的烦死了',
                          properties=pika.BasicProperties(delivery_mode=1,),
                          # 开启强制性标志
                          mandatory=True
                          )

    print("发送用户邮箱到MQ成功, %s" % channel)
except exceptions.UnroutableError as e:
    print('Message was returned', e)
except exceptions.NackError as e:
    print('Message was NackError', e)
except exceptions.StreamLostError as e:
    print('连接不上代理服务器了! MQ突然的停止运行了!', e)
except exceptions.ConnectionClosedByBroker as e:
    print('链接突然的断开了！', e)


connection.close()
