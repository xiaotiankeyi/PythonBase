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

# 2、创建一个名为helloP的队列
channel.queue_declare(queue='HELLOP')
# 3、简单模式,向名为helloP队列中插入用户邮箱地址email
channel.basic_publish(exchange='',      # exchange指定交换机
                      routing_key='HELLOP',
                      body='我真的烦死了',
                      properties={
                          "expiration": 2000   # 消息存活时间
                      }
                      )

print("发送用户邮箱到MQ成功")


connection.close()
