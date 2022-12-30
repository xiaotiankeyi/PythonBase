import pika

# RabbitMQ服务器的连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建一个名为"hello"的队列
channel.queue_declare(queue='hello')

# exchange交换机发送到队列, routing_key指定要发送的队列
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")

connection.close()
