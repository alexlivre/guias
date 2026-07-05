import base64
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

from src.config import MINIMAX_API_KEY

load_dotenv()

API_URL = "https://api.minimax.io/v1/image_generation"
OUTPUT_DIR = Path("img")


def generate_images(
    prompt: str,
    model: str = "image-01",
    aspect_ratio: str = "16:9",
    response_format: str = "base64",
    n: int = 1,
    seed: int | None = None,
    prompt_optimizer: bool = False,
    timeout: int = 60,
) -> dict:
    payload = {
        "model": model,
        "prompt": prompt,
        "aspect_ratio": aspect_ratio,
        "response_format": response_format,
        "n": n,
        "prompt_optimizer": prompt_optimizer,
    }
    if seed is not None:
        payload["seed"] = seed

    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {MINIMAX_API_KEY}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()


def save_images(data: dict, output_dir: Path = OUTPUT_DIR) -> list[Path]:
    output_dir.mkdir(exist_ok=True)
    images = data["data"].get("image_base64", [])
    arquivos = []
    for i, b64 in enumerate(images):
        path = output_dir / f"imagem-{i+1:02d}.jpeg"
        path.write_bytes(base64.b64decode(b64))
        arquivos.append(path)
    return arquivos


def generate_and_save(
    prompt: str,
    aspect_ratio: str = "16:9",
    n: int = 1,
    seed: int | None = None,
    prompt_optimizer: bool = False,
) -> list[Path]:
    data = generate_images(
        prompt=prompt,
        aspect_ratio=aspect_ratio,
        n=n,
        seed=seed,
        prompt_optimizer=prompt_optimizer,
    )
    return save_images(data)


def generate_with_retry(
    prompt: str,
    max_retry: int = 3,
    timeout: int = 30,
) -> dict:
    payload = {
        "model": "image-01",
        "prompt": prompt,
        "aspect_ratio": "16:9",
        "response_format": "base64",
    }

    for tentativa in range(1, max_retry + 1):
        try:
            resp = requests.post(
                API_URL,
                headers={
                    "Authorization": f"Bearer {MINIMAX_API_KEY}",
                    "Content-Type": "application/json",
                },
                json=payload,
                timeout=timeout,
            )
            data = resp.json()
            base = data.get("base_resp", {})
            code = base.get("status_code")

            if code == 0:
                return data

            if code == 1002:
                print(f"Rate limit (1002), tentativa {tentativa}/{max_retry}")
                time.sleep(60)
                continue
            if code == 2045:
                print(f"Growth limit (2045), tentativa {tentativa}/{max_retry}")
                time.sleep(30)
                continue
            if code in (1004, 2049):
                raise SystemExit(f"Erro de autenticação: {code}")
            if code in (1026, 1027):
                raise ValueError(
                    f"Prompt bloqueado: {base.get('status_msg')}"
                )
            return data

        except requests.exceptions.Timeout:
            if tentativa < max_retry:
                print(f"Timeout, tentativa {tentativa}/{max_retry}")
                time.sleep(10)
            else:
                raise

    raise RuntimeError(f"Falha após {max_retry} tentativas")
