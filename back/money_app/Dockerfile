FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/home

RUN apt update -y \
    && apt upgrade -y \
    && apt install -y \
    netcat-traditional

COPY requirements /home
COPY entrypoint.sh /home

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /home/requirements

RUN chmod +x /home/entrypoint.sh
ENTRYPOINT ["/home/entrypoint.sh"]