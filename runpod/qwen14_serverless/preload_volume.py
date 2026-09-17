#!/usr/bin/env python3
"""Preload Qwen3-14B tokenizer/model metadata into the mounted RunPod volume cache.

Run this once on a setup pod with the same network volume mounted. The full model
weights are downloaded by from_pretrained during this script.
"""

import os
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

BASE_MODEL = os.getenv("BASE_MODEL", "Qwen/Qwen3-14B")
HF_HOME = os.getenv("HF_HOME", "/runpod-volume/huggingface")
os.environ.setdefault("HF_HOME", HF_HOME)
os.environ.setdefault("HF_HUB_CACHE", str(Path(HF_HOME) / "hub"))
os.environ.setdefault("TRANSFORMERS_CACHE", str(Path(HF_HOME) / "transformers"))

quantization = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)
print(f"Preloading tokenizer for {BASE_MODEL} into {HF_HOME}")
AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
print(f"Preloading model for {BASE_MODEL} into {HF_HOME}")
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    quantization_config=quantization,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
)
del model
print("Done.")
