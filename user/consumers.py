import json
import pika
import django
import os
from sys import path

from core.models import User
from django.db.models import F


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        "localhost", heartbeat=600, blocked_connection_timeout=300
    )
)
channel = connection.channel()
channel.queue_declare(queue="users")


def callback(channel, method, properties, body):
    print("Received in users...")
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == "portfolio_created":
        user = User.objects.filter(pk=data["user_id"])
        print("user portfolio created")
        user.portfolio_count = F("portfolio_count") + 1
        user.save()
        print("portfolio count increased")
    elif properties.content_type == "portfolio_updated":
        # Do nothing since the portfolio is unchanged.
        ...
    elif properties.content_type == "portfolio_deleted":
        user = User.objects.filter(pk=data["user_id"])
        print("User portfolio deleted")
        user.portfolio_count = F("portfolio_count") - 1
        user.save()
        print("portfolio count reduced")


channel.basic_consume(queue="users", on_message_callback=callback, auto_ack=True)
print("Started consuming...")
# Start receiving messages
channel.start_consuming()
