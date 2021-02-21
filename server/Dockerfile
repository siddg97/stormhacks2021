FROM ubuntu:20.04
WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && \
    apt-get install -y build-essential python3.8 python3-pip python3.8-dev ffmpeg

COPY ./requirements.txt ./requirements.txt

RUN pip3 install --upgrade setuptools pip cython
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT ["python3"]

CMD ["server.py"]