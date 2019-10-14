import util
import threading
import importlib
import time
import logging


def call_class(protocol, host, port, topic):
    mod = importlib.import_module('{}_client'.format(protocol))
    mod = getattr(mod, '{}Client'.format(protocol.capitalize()))
    return mod(host, port, topic)


host = util.get_server_host()
port = util.get_server_port()
topic = util.get_topic()
protocol = util.get_protocol()
thread_num = util.get_thread_num()
verbose = util.get_verbose()

client = call_class(protocol, host, port, topic)

print('Start Pub/Sub with {}'.format(protocol.upper()))

lock = threading.Lock()
for i in range(thread_num):
    t_send = threading.Thread(target=client.send_data, args=[i, lock])
    t_send.daemon = True
    t_send.start()
for i in range(thread_num):
    t_receive = threading.Thread(target=client.receive_data, args=[i, lock, verbose])
    t_receive.daemon = True
    t_receive.start()

current_active_threads_number = 0
try:
    while True:
        current_active_threads_number = len(threading.enumerate()) - 1
        print('The number of current active threads: {}'.format(current_active_threads_number))
        time.sleep(1)
except KeyboardInterrupt:
    print('\nThe last connection num: {}'.format(current_active_threads_number))


