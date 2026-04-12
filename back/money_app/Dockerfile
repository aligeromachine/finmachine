FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/home

RUN apt update -y \
    && apt upgrade -y \
    && apt install -y \
    netcat-traditional \
    git \
    # libpq5 \
    build-essential \
    # Очистка кэша apt для уменьшения размера образа
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Добавляем uv в PATH
ENV PATH="/root/.cargo/bin:/root/.local/bin:${PATH}"

WORKDIR /home/src

COPY requirements /home
COPY entrypoint.sh /home

# Устанавливаем пакеты через uv
RUN uv pip install --system -r /home/requirements --no-cache-dir

RUN chmod +x /home/entrypoint.sh
ENTRYPOINT ["/home/entrypoint.sh"]