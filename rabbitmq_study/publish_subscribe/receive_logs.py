import pika

credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.0.121', port=5672, credentials=credentials))
channel = connection.channel()

# 定义一个交换机logs,扇型交换机
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 生成一个匿名队列
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# 交换机与匿名队列绑定
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


# 回调函数
def callback(ch, method, properties, body):
    print(" [x] %r" % body)


# 发送消息
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
