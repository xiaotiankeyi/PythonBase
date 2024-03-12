import pika
import sys
import os


def main():
    credentials = pika.PlainCredentials('admin', 'admin')
    # 1、连接rabbitmq服务器
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.0.121', port=5672, credentials=credentials))
    channel = connection.channel()

    # 声明队列
    channel.queue_declare(queue='hello', durable=False,
                          exclusive=False, auto_delete=False,
                          arguments={
                              "x-message-ttl": 60000    # 队列存活时间
                          })

    # 定义一个回调函数?当获得消息时?Pika库调用这个回调函数来处理消息

    def callback(ch, method, properties, body):
        # print("==ch表示管道内存地址", ch)
        # print("==", method)
        # print("==", properties)
        ch.basic_ack(delivery_tag=method.delivery_tag)      # 手动ack
        # print(dir(properties))
        # print("手动ack:", method.delivery_tag)
        print("receive message", body.decode())

    # 消费消息
    channel.basic_consume(
        "hello",
        callback,  # 回调地址(函数)
        auto_ack=False   # TRUE自动ack机制,告诉队列完成了
    )

    # 等待消息
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
