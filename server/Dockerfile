FROM python:slim
WORKDIR /app

# Disable Debian UI Prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install External Tools
RUN apt-get update -y && \
    apt-get install -y build-essential ffmpeg cmake

# Install Requirements
ADD ./requirements.txt ./requirements.txt

RUN pip3 install --upgrade setuptools pip cython
RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python3", "server.py"]