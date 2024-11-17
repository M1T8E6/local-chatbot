FROM python:3.12-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \   
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* && \
    curl https://ollama.ai/install.sh | sh

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501 11434

CMD ["tail", "-f", "/dev/null"]