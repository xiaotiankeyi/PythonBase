import sys
import os
import pika


def main():
    credentials = pika.PlainCredentials('admin', 'admin')
    # 1、连接rabbitmq服务器连接
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.0.121', port=5672, credentials=credentials))

    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    # 生成5个队列
    queues0bj = []
    for i in range(5):
        case = f"case_{i}"
        case = channel.queue_declare(queue=f"case_{i}", exclusive=True)
        queues0bj.append(case)

    routing = ["#", "info.*", "#.warning.*", "*.error.#", "*.#"]

    # 绑定关系交换机,队列,路由
    for queue, routing_key in zip(queues0bj, routing):
        channel.queue_bind(exchange='topic_logs',
                           queue=queue.method.queue,
                           routing_key=routing_key)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body,))

    for queue in queues0bj:
        channel.basic_consume(
            queue=queue.method.queue, on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
