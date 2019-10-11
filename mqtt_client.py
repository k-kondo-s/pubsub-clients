import paho.mqtt.client as mqtt
from time import sleep
from datetime import datetime
import threading


class MqttClient:
    def __init__(self, host, port, topic):
        self.host = host
        self.port = port
        self.topic = topic

    def send_data(self, thread_num):
        def on_connect(client, userdata, flag, rc):
            pass

        def on_disconnect(client, userdata, flag, rd):
            print("Unexpected disconnection occurred")

        def on_publish():
            print("published")

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.on_publish = on_publish
        client.connect(self.host, self.port, 60)
        client.loop_start()
        print('PUB ThureadNum: {}, ThreadId: {}'.format(thread_num, threading.get_ident()))
        while True:
            client.publish(self.topic, 'PUB ThreadNum {} sent at {}'.format(thread_num, str(datetime.now())))
            sleep(1)

    def receive_data(self, thread_num):
        def on_connect(client, userdata, flag, rc):
            client.subscribe('topic/test')

        def on_disconnect(client, userdata, flag, rc):
            if rc != 0:
                print("Disconnected")

        def on_message(client, userdata, msg):
            print('SUB ThreadNum {} received "{}" at {}'.format(thread_num, msg.payload, str(datetime.now())))

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_disconnect = on_disconnect
        client.on_message = on_message
        client.connect(self.host, self.port, 60)
        print('SUB ThureadNum: {}, ThreadId: {}'.format(thread_num, threading.get_ident()))
        client.loop_forever()
