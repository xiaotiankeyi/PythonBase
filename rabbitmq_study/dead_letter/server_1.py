from case import RabbitMQClient

if __name__ == "__main__":
    channel = RabbitMQClient()
    exchange_name = 'exchange_topic'
    channel.declare_exchange(exchange_name, durable=True)

    body = "hello 这个是发送给info01队列的信息,会被info01正常消费"

    channel.basic_publish(
        exchange=exchange_name,
        routing_key="info01",
        body=body
    )

    channel.close_channel()
