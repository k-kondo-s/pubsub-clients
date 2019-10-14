import os
from distutils.util import strtobool

target_host = 'T_HOST'
target_port = 'T_PORT'
target_topic = 'T_TOPIC'
target_protocol = 'T_PROTOCOL'
target_thread_num = 'T_THREAD_NUM'
target_verbose = 'T_VERBOSE'


def get_env_var(name):
    if name in os.environ:
        return os.environ[name]
    else:
        print('Environment variable is not set: {}'.format(name))


def get_server_host():
    return str(get_env_var(target_host)) if get_env_var(target_host) is not None else '172.28.128.3'


def get_server_port():
    return int(get_env_var(target_port)) if get_env_var(target_port) is not None else 1883


def get_topic():
    return str(get_env_var(target_topic)) if get_env_var(target_topic) is not None else 'topic/test'


def get_protocol():
    return str(get_env_var(target_protocol)) if get_env_var(target_protocol) is not None else 'mqtt'


def get_thread_num():
    return int(get_env_var(target_thread_num)) if get_env_var(target_thread_num) is not None else 2


def get_verbose():
    return strtobool(get_env_var(target_verbose))
