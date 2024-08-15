FROM python:3.11-slim

# Install common utilities
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    wget \
    software-properties-common

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /workspace

# Configure pip to use Tsinghua University's mirror
RUN mkdir -p ~/.pip/ && \
    echo "[global]\nindex-url = https://pypi.tuna.tsinghua.edu.cn/simple" > ~/.pip/pip.conf

# Install required Python packages
RUN pip install --no-cache-dir numpy pandas yfinance