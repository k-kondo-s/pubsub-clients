import paho.mqtt.client as mqtt
from time import sleep
from datetime import datetime
import threading


class MqttClient:

    USER = 'guest'
    PASSWORD = 'guest'

    def __init__(self, host, port, topic):
        self.host = host
        self.port = port
        self.topic = topic
        self.USER = 'guest'
        self.PASSWORD = 'guest'

    def send_data(self, thread_num, lock):
        def on_connect(client, userdata, flag, rc):
            pass

        def on_disconnect(client, userdata, flag, rd):
            print("Unexpected disconnection occurred")

        def on_publish():
            print("published")

        lock.acquire()
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.on_publish = on_publish
        client.username_pw_set(self.USER, self.PASSWORD)
        client.connect(self.host, self.port, 60)
        client.loop_start()
        print('PUB MQTT ThreadNum: {}, ThreadId: {}'.format(thread_num, threading.get_ident()))
        lock.release()
        while True:
            client.publish(self.topic, 'PUB ThreadNum {} sent at {}'.format(thread_num, str(datetime.now())))
            sleep(1)

    def receive_data(self, thread_num, lock, verbose):
        def on_connect(client, userdata, flag, rc):
            client.subscribe(self.topic)

        def on_disconnect(client, userdata, flag, rc):
            if rc != 0:
                print("Disconnected")

        def on_message(client, userdata, msg):
            if verbose:
                print('SUB MQTT ThreadNum {} received "{}" at {}'.format(thread_num, msg.payload, str(datetime.now())))
            else:
                pass

        lock.acquire()
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.on_message = on_message
        client.username_pw_set(self.USER, self.PASSWORD)
        client.connect(self.host, self.port, 60)
        print('SUB MQTT ThreadNum: {}, ThreadId: {}'.format(thread_num, threading.get_ident()))
        lock.release()
        client.loop_forever()
