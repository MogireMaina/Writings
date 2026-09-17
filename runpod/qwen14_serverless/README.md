# Qwen14 RunPod Serverless Humanizer

This package deploys the selected Qwen transformer as a RunPod serverless worker.
It loads `Qwen/Qwen3-14B` in 4-bit and optionally applies the LoRA adapter at:

`/runpod-volume/adapters/qwen3-14b-chat-style-lora-compact-r16`

## Why this layout

- Docker image contains Python/CUDA dependencies and handler code.
- RunPod network volume contains Hugging Face model cache and LoRA adapter.
- Serverless workers can scale to zero, then cold-start by loading from the mounted volume instead of reinstalling or transferring files each time.

## Volume layout

Recommended mounted volume paths:

```text
/runpod-volume/huggingface/...
/runpod-volume/adapters/qwen3-14b-chat-style-lora-compact-r16/adapter_config.json
/runpod-volume/adapters/qwen3-14b-chat-style-lora-compact-r16/adapter_model.safetensors
```

Preload the base model once on a setup pod with the same volume mounted:

```bash
cd /app
python3 preload_volume.py
```

Copy the adapter once:

```bash
mkdir -p /runpod-volume/adapters/qwen3-14b-chat-style-lora-compact-r16
cp -a /workspace/gemma-style-training/artifacts/qwen3-14b-chat-style-lora-compact-r16/* \
  /runpod-volume/adapters/qwen3-14b-chat-style-lora-compact-r16/
```

## Build image

```bash
docker build -t qwen14-humanizer-serverless:latest qwen14_serverless
```

Push to your registry, then create a RunPod Serverless/Flex endpoint from that image.

## Environment variables

```text
BASE_MODEL=Qwen/Qwen3-14B
ADAPTER_PATH=/runpod-volume/adapters/qwen3-14b-chat-style-lora-compact-r16
HF_HOME=/runpod-volume/huggingface
DEFAULT_BATCH_SIZE=128
ALLOWED_BATCH_SIZES=16,32,64,128
MAX_SENTENCES_PER_JOB=512
MAX_INPUT_LENGTH=1024
```

If `ADAPTER_PATH` is empty or missing, the worker uses the base model only.

## Request examples

Batch 16:

```json
{
  "input": {
    "sentences": ["Pip is shaped by the society around him."],
    "batch_size": 16,
    "style": "scholar",
    "temperature": 0.9,
    "top_p": 0.9,
    "candidates": 1,
    "max_new_tokens": 192
  }
}
```

Batch 32, 64, or 128 uses the same schema:

```json
{
  "input": {
    "sentences": ["Sentence one.", "Sentence two."],
    "batch_size": 128,
    "style": "scholar"
  }
}
```

Custom prompt:

```json
{
  "input": {
    "sentences": ["Sentence one."],
    "batch_size": 128,
    "system_prompt": "You rewrite sentences for naturalness while preserving exact meaning.",
    "temperature": 0.9,
    "top_p": 0.9
  }
}
```

Health check:

```json
{"input": {"health": true}}
```

## Expected speed from our A40 tests

For 128 sentence-level rewrites:

- Qwen3-14B base: about `9.20 sentences/sec` generation-only.
- Qwen3-14B + LoRA adapter: about `8.61 sentences/sec` generation-only.

Cold start also includes model load time. With cached weights and adapter already mounted, expect roughly tens of seconds for load, then warm requests use the generation speed above.

## Batch guidance

- `16`: safer for long sentences or smaller GPUs.
- `32`: conservative default if latency matters.
- `64`: good middle ground.
- `128`: best throughput observed on A40 for this workload.

For long sentences or multiple candidates, reduce batch size first before reducing `max_new_tokens`.

## Calling from this laptop

Create a local env file. Do not commit real values:

```bash
cp qwen14_serverless/.env.example qwen14_serverless/.env
```

Fill in:

```text
RUNPOD_ENDPOINT_ID=your_endpoint_id
RUNPOD_API_KEY=your_runpod_api_key
```

Run one sentence asynchronously with polling:

```bash
python3 qwen14_serverless/test_client.py \
  --sentence "Pip is shaped by the class system into which he is born." \
  --batch-size 128 \
  --style scholar
```

Run with `/runsync`:

```bash
python3 qwen14_serverless/test_client.py --sync \
  --sentence "Pip is shaped by the class system into which he is born."
```

Run a file with one sentence per line:

```bash
python3 qwen14_serverless/test_client.py \
  --input-file sentences.txt \
  --batch-size 128 \
  --temperature 0.9 \
  --top-p 0.9
```

Raw curl async call:

```bash
curl -s -X POST "https://api.runpod.ai/v2/$RUNPOD_ENDPOINT_ID/run" \
  -H "Authorization: Bearer $RUNPOD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "sentences": ["Pip is shaped by the class system into which he is born."],
      "batch_size": 128,
      "style": "scholar",
      "temperature": 0.9,
      "top_p": 0.9,
      "candidates": 1,
      "max_new_tokens": 192
    }
  }'
```

Then poll:

```bash
curl -s -X POST "https://api.runpod.ai/v2/$RUNPOD_ENDPOINT_ID/status/$JOB_ID" \
  -H "Authorization: Bearer $RUNPOD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```
