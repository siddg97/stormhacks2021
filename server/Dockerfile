FROM ubuntu:16.04
WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]

CMD ["server.py"]