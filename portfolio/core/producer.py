import json
import pika


# Establish a connection with the rabbitMQ server
connection = pika.BlockingConnection(
    # pika.ConnectionParameters(
    #     "localhost", heartbeat=600, blocked_connection_timeout=300
    # )
)
channel = connection.channel()


def publish(method, body):
    """

    Args:
        method (_type_): information about the message
        body (_type_): the message to be sent
    """
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="",
        routing_key="users",
        body=json.dumps(body),
        properties=properties,
    )
