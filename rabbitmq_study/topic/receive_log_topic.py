import pika
import sys

credentials = pika.PlainCredentials('admin', 'admin')
# 1、连接rabbitmq服务器连接
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.0.121', port=5672, credentials=credentials))

channel = connection.channel()

# 定义交换机
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

# 生成匿名队列,durable=True队列持久化,exclusive是否排外
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

binding_keys = sys.argv[1:]
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
    sys.exit(1)

# 接收外部参数,让交换机和队列绑定
for binding_key in binding_keys:
    channel.queue_bind(
        exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
