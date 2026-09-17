#!/usr/bin/env python3
"""Local test client for the Qwen14 RunPod serverless endpoint."""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def post_json(url: str, api_key: str, payload: dict, timeout: int) -> dict:
    body = json.dumps(payload).encode("utf-8")
    req = Request(
        url,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", type=Path, default=Path("qwen14_serverless/.env"))
    parser.add_argument("--endpoint-id", default=os.getenv("RUNPOD_ENDPOINT_ID"))
    parser.add_argument("--api-key", default=os.getenv("RUNPOD_API_KEY"))
    parser.add_argument("--sentence", action="append", help="Sentence to rewrite. Can be repeated.")
    parser.add_argument("--input-file", type=Path, help="Text file with one sentence per line.")
    parser.add_argument("--batch-size", type=int, default=int(os.getenv("QWEN14_BATCH_SIZE", "128")))
    parser.add_argument("--style", default=os.getenv("QWEN14_STYLE", "scholar"))
    parser.add_argument("--temperature", type=float, default=float(os.getenv("QWEN14_TEMPERATURE", "0.9")))
    parser.add_argument("--top-p", type=float, default=float(os.getenv("QWEN14_TOP_P", "0.9")))
    parser.add_argument("--candidates", type=int, default=int(os.getenv("QWEN14_CANDIDATES", "1")))
    parser.add_argument("--max-new-tokens", type=int, default=int(os.getenv("QWEN14_MAX_NEW_TOKENS", "192")))
    parser.add_argument("--sync", action="store_true", help="Use /runsync instead of async /run + /status polling.")
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--poll-interval", type=float, default=2.0)
    args = parser.parse_args()

    load_dotenv(args.env)
    endpoint_id = args.endpoint_id or os.getenv("RUNPOD_ENDPOINT_ID")
    api_key = args.api_key or os.getenv("RUNPOD_API_KEY")
    if not endpoint_id:
        raise SystemExit("Missing RUNPOD_ENDPOINT_ID")
    if not api_key:
        raise SystemExit("Missing RUNPOD_API_KEY")

    sentences = []
    if args.input_file:
        sentences.extend([line.strip() for line in args.input_file.read_text().splitlines() if line.strip()])
    if args.sentence:
        sentences.extend(args.sentence)
    if not sentences:
        sentences = ["Pip is shaped by the class system into which he is born."]

    payload = {
        "input": {
            "sentences": sentences,
            "batch_size": args.batch_size,
            "style": args.style,
            "temperature": args.temperature,
            "top_p": args.top_p,
            "candidates": args.candidates,
            "max_new_tokens": args.max_new_tokens,
        }
    }

    base = f"https://api.runpod.ai/v2/{endpoint_id}"
    started = time.perf_counter()
    try:
        if args.sync:
            response = post_json(f"{base}/runsync", api_key, payload, args.timeout)
        else:
            submitted = post_json(f"{base}/run", api_key, payload, args.timeout)
            job_id = submitted.get("id")
            if not job_id:
                print(json.dumps(submitted, indent=2), file=sys.stderr)
                raise SystemExit("RunPod did not return a job id")
            while True:
                response = post_json(f"{base}/status/{job_id}", api_key, {}, args.timeout)
                status = response.get("status")
                if status in {"COMPLETED", "FAILED", "CANCELLED", "TIMED_OUT"}:
                    break
                time.sleep(args.poll_interval)
    except HTTPError as exc:
        print(exc.read().decode("utf-8", errors="replace"), file=sys.stderr)
        raise
    except URLError as exc:
        raise SystemExit(f"Request failed: {exc}") from exc

    response["client_elapsed_seconds"] = round(time.perf_counter() - started, 3)
    print(json.dumps(response, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
