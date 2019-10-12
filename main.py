import util
import threading
import importlib


def call_class(protocol, host, port, topic):
    mod = importlib.import_module('{}_client'.format(protocol))
    mod = getattr(mod, 'MqttClient'.format(protocol))
    return mod(host, port, topic)


host = util.get_server_host()
port = util.get_server_port()
topic = util.get_topic()
protocol = util.get_protocol()
thread_num = util.get_thread_num()

client = call_class(protocol, host, port, topic)

for i in range(thread_num):
    t_send = threading.Thread(target=client.send_data, args=[i])
    t_receive = threading.Thread(target=client.receive_data, args=[i])
    t_send.start()
    t_receive.start()
