FROM n8nio/n8n:latest

USER root

# Системные зависимости
RUN apk add --no-cache ffmpeg python3 py3-pip curl

# Установка Deno
RUN curl -fsSL https://deno.land/install.sh   | sh

# Установка yt-dlp с поддержкой EJS (JavaScript)
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir "yt-dlp[default]" && \
    ln -s /opt/venv/bin/yt-dlp /usr/local/bin/yt-dlp

RUN /opt/venv/bin/pip install requests

# PATH для Deno
ENV PATH="/root/.deno/bin:${PATH}"