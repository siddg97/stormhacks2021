FROM python:3.8.5-slim
WORKDIR /app

# Disable Debian UI Prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install External Tools
RUN apt-get update -y && \
    apt-get install -y build-essential ffmpeg cmake && \
    pip3 install --upgrade setuptools pip cython

# Install Requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python3", "wsgi.py"]