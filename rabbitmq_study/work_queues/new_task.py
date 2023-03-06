import pika
import sys

credentials = pika.PlainCredentials('admin', 'admin')
# 1、连接rabbitmq服务器连接
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.0.121', port=5672, credentials=credentials))

channel = connection.channel()

# durable=True队列持久化
# exclusive=False 当消费者断开连接到时候,队列是否清除
channel.queue_declare(queue='task_queue', durable=True, exclusive=False)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        # Server因意外重启，未处理的消息也不会丢失
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent %r" % message)
connection.close()
