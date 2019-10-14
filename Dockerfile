FROM python:3

RUN apt-get update && apt-get install --no-install-recommends -y \
    python-pip \
 && rm -rf /var/lib/apt/lists/*

COPY *.py /
COPY requirements.txt /

RUN pip install -r /requirements.txt

ENV TZ="Asia/Tokyo"

ENTRYPOINT ["python", "/main.py"]