import sys
import os
import pika


def main():
    credentials = pika.PlainCredentials('admin', 'admin')
    # 1、连接rabbitmq服务器连接
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.0.121', port=5672, credentials=credentials))

    channel = connection.channel()

    channel.exchange_declare(exchange='direct_logs',
                             exchange_type='direct')

    case_1 = channel.queue_declare(queue="case_1", exclusive=True)
    case_2 = channel.queue_declare(queue="case_2", exclusive=True)
    case_3 = channel.queue_declare(queue="case_3", exclusive=True)

    queueObj = [case_1, case_2, case_3]
    routing = ["info", "warning", "error"]

    # 绑定关系交换机,队列,路由
    for queue, routing_key in zip(queueObj, routing):
        channel.queue_bind(exchange='direct_logs',
                           queue=queue.method.queue,
                           routing_key=routing_key)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] %r:%r" % (method.routing_key, body,))
        # pathlist = os.listdir(os.getcwd())
        # pathfile = [val for val in pathlist if val.endswith("log")][0]
        # if pathfile:
        #     with open(file=pathfile, mode="ab+") as f:
        #         f.write(body)

    for queue in queueObj:
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
