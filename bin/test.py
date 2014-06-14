# encoding: utf-8
import pika
import sys
from postboy import Email

sys.path.append('..')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

def handler(*args):
    print args

channel = connection.channel()
channel.queue_declare(queue='postboy')

channel.basic_publish(
    exchange='',
    routing_key='postboy',
    body=Email('test@user.com', 'me@mosquito.su', "Test").dumps(),
    properties=pika.BasicProperties(delivery_mode=2)
)

channel.close()