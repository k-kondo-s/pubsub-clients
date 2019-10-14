# Description

MQTT and AMQP clients running with multiple threads.

# Run

With docker

```bash
docker run --rm --name pubsub-clients \
    -e T_HOST=172.28.128.3 \
    -e T_PORT=1883 \
    -e T_PROTOCOL=mqtt \
    -e T_TOPIC="topic/test" \
    -e T_THREAD_NUM=3 \
    -e T_VERBOSE=True \
    kenchaaan/pubsub-clients
```

directly

```bash
T_HOST=172.28.128.3 \
T_PORT=1883 \
T_PROTOCOL=mqtt \
T_TOPIC="topic/test" \
T_THREAD_NUM=2 \
T_VERBOSE=True \
venv/bin/python main.py
```

# Environment Variables

|NAME|Description|Default|
|---|---|---|
|`T_HOST`|Host name or IP address|172.28.128.3|
|`T_PORT`|Port number|1883|
|`T_TOPIC`|Topic name|topic/test|
|`T_PROTOCOL`|Protocol name that is either `mqtt` or `amqp`|`mqtt`|
|`T_THREAD_NUM`|The number of threads that you would run simultaneously|2|
|`T_VERBOSE`|Switch whether it shows messages which get by subscribing|False|

# (Appendix) Run RabbitMQ with MQTT

```bash
docker run -d --name rbmq \
    -p 4369:4369 \
    -p 25672:25672 \
    -p 5671:5671 \
    -p 5672:5672 \
    -p 1883:1883 \
    -e RABBITMQ_DEFAULT_USER=guest \
    -e RABBITMQ_DEFAULT_PASS=guest \
    kenchaaan/rabbitmq-mqtt
``` 