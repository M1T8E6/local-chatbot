FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install required system dependencies and Ollama 
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \   
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* && \
    curl https://ollama.ai/install.sh | sh

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create startup script
RUN echo '#!/bin/bash\n\
ollama serve &\n\
sleep 5 &&\n\
ollama run llama3.2 &\n\
make run' > /app/start.sh && \
    chmod +x /app/start.sh

# Expose Streamlit port and Ollama port
EXPOSE 8501 11434

# Command to run both services
CMD ["/app/start.sh"]
