#!/usr/bin/env python3
"""RunPod serverless handler for Qwen3-14B sentence rewriting.

Expected RunPod input:
{
  "sentences": ["Sentence one.", "Sentence two."],
  "batch_size": 128,
  "style": "scholar",
  "temperature": 0.9,
  "top_p": 0.9,
  "candidates": 1,
  "max_new_tokens": 192
}
"""

import os
import re
import time
from datetime import datetime, timezone
from typing import Any

import runpod

BASE_MODEL = os.getenv("BASE_MODEL", "Qwen/Qwen3-14B")
ADAPTER_PATH = os.getenv(
    "ADAPTER_PATH",
    "/runpod-volume/adapters/qwen3-14b-chat-style-lora-compact-r16",
)
HF_HOME = os.getenv("HF_HOME", "/runpod-volume/huggingface")
MAX_INPUT_LENGTH = int(os.getenv("MAX_INPUT_LENGTH", "1024"))
DEFAULT_BATCH_SIZE = int(os.getenv("DEFAULT_BATCH_SIZE", "128"))
ALLOWED_BATCH_SIZES = {
    int(value.strip())
    for value in os.getenv("ALLOWED_BATCH_SIZES", "16,32,64,128").split(",")
    if value.strip()
}
MAX_SENTENCES_PER_JOB = int(os.getenv("MAX_SENTENCES_PER_JOB", "512"))

os.environ.setdefault("HF_HOME", HF_HOME)
os.environ.setdefault("HF_HUB_CACHE", os.path.join(HF_HOME, "hub"))
os.environ.setdefault("TRANSFORMERS_CACHE", os.path.join(HF_HOME, "transformers"))

STYLES = {
    "scholar": "You rewrite sentences for academic clarity, precision, and natural scholarly flow while preserving exact meaning.",
    "orwell": "You are a George Orwell who reconstructs sentences for highest semantic, grammatic and natural flow.",
    "hemingway": "You are an Ernest Hemingway who rewrites sentences for correct meaning, good grammar and natural flow.",
    "default": "You rewrite sentences for naturalness while preserving exact meaning.",
}

_model = None
_tokenizer = None
_load_info: dict[str, Any] | None = None


def clean_output(text: str) -> str:
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"^assistant\s*", "", text.strip(), flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", text).strip()


def get_model():
    global _model, _tokenizer, _load_info
    if _model is not None and _tokenizer is not None:
        return _tokenizer, _model

    import torch
    from peft import PeftModel
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

    started = time.perf_counter()
    quantization = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
    tokenizer.padding_side = "left"
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL,
        quantization_config=quantization,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        trust_remote_code=True,
    )
    base_loaded = time.perf_counter()
    adapter_loaded = False
    adapter_seconds = 0.0
    if ADAPTER_PATH and os.path.exists(ADAPTER_PATH):
        adapter_started = time.perf_counter()
        model = PeftModel.from_pretrained(model, ADAPTER_PATH)
        adapter_seconds = time.perf_counter() - adapter_started
        adapter_loaded = True
    model.eval()

    _tokenizer = tokenizer
    _model = model
    _load_info = {
        "base_model": BASE_MODEL,
        "adapter_path": ADAPTER_PATH,
        "adapter_loaded": adapter_loaded,
        "base_model_load_seconds": round(base_loaded - started, 3),
        "adapter_load_seconds": round(adapter_seconds, 3),
        "total_load_seconds": round(time.perf_counter() - started, 3),
        "loaded_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    return _tokenizer, _model


def make_prompt(tokenizer, system_prompt: str, sentence: str) -> str:
    try:
        return tokenizer.apply_chat_template(
            [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": sentence},
            ],
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,
        )
    except TypeError:
        return tokenizer.apply_chat_template(
            [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": sentence},
            ],
            tokenize=False,
            add_generation_prompt=True,
        )


def parse_input(event: dict[str, Any]) -> dict[str, Any]:
    payload = event.get("input") or {}
    if payload.get("health"):
        return {"health": True}

    sentences = payload.get("sentences") or payload.get("texts") or payload.get("items")
    if isinstance(sentences, str):
        sentences = [sentences]
    if not isinstance(sentences, list) or not sentences:
        raise ValueError("input.sentences must be a non-empty string or list of strings")

    normalized = []
    for idx, item in enumerate(sentences, start=1):
        if isinstance(item, dict):
            text = str(item.get("text") or "").strip()
            source_id = item.get("id") or item.get("source_id") or idx
        else:
            text = str(item).strip()
            source_id = idx
        if text:
            normalized.append({"id": source_id, "text": text})
    if not normalized:
        raise ValueError("input.sentences contained no non-empty text")
    if len(normalized) > MAX_SENTENCES_PER_JOB:
        raise ValueError(f"too many sentences: {len(normalized)} > {MAX_SENTENCES_PER_JOB}")

    batch_size = int(payload.get("batch_size", DEFAULT_BATCH_SIZE))
    if batch_size not in ALLOWED_BATCH_SIZES:
        raise ValueError(f"batch_size must be one of {sorted(ALLOWED_BATCH_SIZES)}")

    style = str(payload.get("style", "scholar")).strip().lower()
    system_prompt = payload.get("system_prompt") or STYLES.get(style)
    if not system_prompt:
        raise ValueError(f"unknown style {style!r}; use one of {sorted(STYLES)} or pass system_prompt")

    return {
        "health": False,
        "sentences": normalized,
        "batch_size": batch_size,
        "style": style,
        "system_prompt": system_prompt,
        "temperature": float(payload.get("temperature", 0.9)),
        "top_p": float(payload.get("top_p", 0.9)),
        "candidates": int(payload.get("candidates", 1)),
        "max_new_tokens": int(payload.get("max_new_tokens", 192)),
        "return_original": bool(payload.get("return_original", True)),
    }


def handler(event: dict[str, Any]) -> dict[str, Any]:
    request_started = time.perf_counter()
    parsed = parse_input(event)
    if parsed.get("health"):
        return {"ok": True, "model_loaded": _model is not None, "load_info": _load_info}

    tokenizer, model = get_model()
    generation_started = time.perf_counter()
    results = []
    total_outputs = len(parsed["sentences"]) * parsed["candidates"]

    for candidate_index in range(parsed["candidates"]):
        for start in range(0, len(parsed["sentences"]), parsed["batch_size"]):
            batch = parsed["sentences"][start : start + parsed["batch_size"]]
            prompts = [make_prompt(tokenizer, parsed["system_prompt"], item["text"]) for item in batch]
            encoded = tokenizer(
                prompts,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=MAX_INPUT_LENGTH,
            ).to(model.device)
            with torch.inference_mode():
                generated = model.generate(
                    **encoded,
                    max_new_tokens=parsed["max_new_tokens"],
                    do_sample=True,
                    temperature=parsed["temperature"],
                    top_p=parsed["top_p"],
                    pad_token_id=tokenizer.pad_token_id,
                    eos_token_id=tokenizer.eos_token_id,
                )
            prompt_length = encoded["input_ids"].shape[1]
            for item, output in zip(batch, generated):
                rewritten = tokenizer.decode(output[prompt_length:], skip_special_tokens=True)
                row = {
                    "id": item["id"],
                    "candidate_index": candidate_index + 1,
                    "transformed_text": clean_output(rewritten),
                }
                if parsed["return_original"]:
                    row["original_text"] = item["text"]
                results.append(row)

    generation_seconds = time.perf_counter() - generation_started
    total_seconds = time.perf_counter() - request_started
    return {
        "results": results,
        "meta": {
            "base_model": BASE_MODEL,
            "adapter_path": ADAPTER_PATH,
            "load_info": _load_info,
            "style": parsed["style"],
            "batch_size": parsed["batch_size"],
            "allowed_batch_sizes": sorted(ALLOWED_BATCH_SIZES),
            "sentences": len(parsed["sentences"]),
            "candidates": parsed["candidates"],
            "total_outputs": total_outputs,
            "temperature": parsed["temperature"],
            "top_p": parsed["top_p"],
            "max_new_tokens": parsed["max_new_tokens"],
            "generation_seconds": round(generation_seconds, 3),
            "total_seconds": round(total_seconds, 3),
            "outputs_per_second_generation": round(total_outputs / generation_seconds, 3) if generation_seconds else None,
        },
    }


runpod.serverless.start({"handler": handler})
