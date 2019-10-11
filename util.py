import os

target_host = 'HOST'
target_port = 'PORT'
target_topic = 'TOPIC'
target_protocol = 'PROTOCOL'


def get_env_var(name):
    if name in os.environ:
        return os.environ[name]
    else:
        print('Unknown environment variable: {}'.format(name))


def get_server_host():
    return str(get_env_var(target_host)) if get_env_var(target_host) is not None else '172.28.128.3'


def get_server_port():
    return int(get_env_var(target_port)) if get_env_var(target_port) is not None else 1883


def get_topic():
    return str(get_env_var(target_topic)) if get_env_var(target_topic) is not None else 'topic/test'


def get_protocol():
    return str(get_env_var(target_protocol)) if get_env_var(target_protocol) is not None else 'mqtt'
