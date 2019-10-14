import pika
import time
from _datetime import datetime
import threading


class AmqpClient:
    def __init__(self, host, port, topic):
        self.host = host
        self.port = port
        self.topic = topic

    def send_data(self, thread_num, lock):
        lock.acquire()
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = connection.channel()

        channel.queue_declare(queue=self.topic)
        print('PUB AMQP ThreadNum: {}, ThreadId: {}'.format(thread_num, threading.get_ident()))
        lock.release()
        while True:
            value = 'PUB ThreadNum {} sent at {}'.format(thread_num, str(datetime.now()))
            channel.basic_publish(exchange='',
                                  routing_key=self.topic,
                                  body=value)
            time.sleep(1)

    def receive_data(self, thread_num, lock, verbose):
        def callback(ch, methoc, properties, body):
            if verbose:
                print('SUB AMQP ThreadNum {} received "{}" at {}'.format(thread_num, body, str(datetime.now())))
            else:
                pass
        lock.acquire()
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host, port=self.port))
        channel = connection.channel()
        channel.queue_declare(queue=self.topic)
        channel.basic_consume(queue=self.topic, auto_ack=True, on_message_callback=callback)
        print('SUB AMQP ThreadNum: {}, ThreadId: {}'.format(thread_num, threading.get_ident()))
        lock.release()
        channel.start_consuming()
