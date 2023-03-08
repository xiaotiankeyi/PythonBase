import pika
import time

# 工作队列模模式之——>轮询分发机制
credentials = pika.PlainCredentials('admin', 'admin')
# 1、连接rabbitmq服务器连接
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.0.121', port=5672, credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)     # durable=True队列持久化
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")


channel.basic_consume(queue='task_queue',
                      on_message_callback=callback, auto_ack=True)

channel.start_consuming()
