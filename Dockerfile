FROM runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    HF_HOME=/runpod-volume/huggingface \
    HF_HUB_CACHE=/runpod-volume/huggingface/hub \
    TRANSFORMERS_CACHE=/runpod-volume/huggingface/transformers \
    BASE_MODEL=Qwen/Qwen3-14B \
    ADAPTER_PATH=/runpod-volume/adapters/qwen3-14b-chat-style-lora-compact-r16 \
    DEFAULT_BATCH_SIZE=128 \
    ALLOWED_BATCH_SIZES=16,32,64,128 \
    MAX_SENTENCES_PER_JOB=512

RUN apt-get update && apt-get install -y --no-install-recommends \
    git curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY runpod/qwen14_serverless/requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install --ignore-installed -r /app/requirements.txt
COPY runpod/qwen14_serverless/handler.py /app/handler.py

CMD ["python3", "/app/handler.py"]
