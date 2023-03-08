import pika
import sys
import os


def main():
    credentials = pika.PlainCredentials('admin', 'admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.0.121', port=5672, credentials=credentials))
    channel = connection.channel()

    # 定义一个交换机logs,扇型交换机
    channel.exchange_declare(exchange='logs', exchange_type='fanout')

    # 生成三个队列
    case_1 = channel.queue_declare(queue='case_1', exclusive=True)
    case_2 = channel.queue_declare(queue='case_2', exclusive=True)
    case_3 = channel.queue_declare(queue='case_3', exclusive=True)

    # 交换机与匿名队列绑定
    channel.queue_bind(exchange='logs', queue=case_1.method.queue)
    channel.queue_bind(exchange='logs', queue=case_2.method.queue)
    channel.queue_bind(exchange='logs', queue=case_3.method.queue)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    # 回调函数
    def case_1_callback(ch, method, properties, body):
        print("case_1接收的信息是:%r" % body)

    def case_2_callback(ch, method, properties, body):
        print("case_2接收的信息是:%r" % body)

    def case_3_callback(ch, method, properties, body):
        print("case_3接收的信息是:%r" % body)

    # 发送消息
    channel.basic_consume(
        queue=case_1.method.queue, on_message_callback=case_1_callback, auto_ack=True)
    channel.basic_consume(
        queue=case_2.method.queue, on_message_callback=case_2_callback, auto_ack=True)
    channel.basic_consume(
        queue=case_3.method.queue, on_message_callback=case_3_callback, auto_ack=True)

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
