from case import RabbitMQClient

if __name__ == "__main__":
    # 对加入死信队列的消息进行消费
    channel = RabbitMQClient()
    queue = "RetryQueue"
    channel.basic_consume(channel.callback_success, queue, auto_ack=False)
    channel.start_consuming()