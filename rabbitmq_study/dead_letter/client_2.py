from case import RabbitMQClient

if __name__ == "__main__":
    channel = RabbitMQClient()
    exchange_name = 'exchange_topic'
    channel.declare_exchange(exchange_name, durable=True)
    queue = "info02"
    channel.declare_delay_queue(queue, TTL=10000)

    channel.bind_queue(queue, exchange_name, 'info02')
    channel.basic_consume(channel.callback_reject, queue, auto_ack=False)
    channel.start_consuming()
