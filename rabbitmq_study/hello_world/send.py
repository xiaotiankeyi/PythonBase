import pika
import base64
import time

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


channel.basic_publish(exchange='',      # exchange指定交换机
                      routing_key='hello',
                      body='我真的烦死了',
                      properties=None
                      )

print("发送用户邮箱到MQ成功")


connection.close()
