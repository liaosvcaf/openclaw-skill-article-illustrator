#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GLM-image generation script for the article-illustrator skill.
Uses Z.AI / BigModel-compatible API only.

Accepted key names:
- preferred: ZAI_API_KEY / zai_api_key
- fallback:  GLM_API_KEY / glm_api_key / api_key
"""

import argparse
import datetime
import json
import os
import re
import sys

import requests

SUPPORTED_LANGUAGES = {
    "zh": "Chinese",
    "en": "English",
    "ja": "Japanese",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
}

GLM_PRICE_STANDARD_CNY = 0.10
GLM_PRICE_HD_CNY = 0.20
CNY_TO_USD = 0.138


def _load_key_from_env_and_configs() -> str | None:
    for env_var in ["ZAI_API_KEY", "GLM_API_KEY"]:
        value = os.environ.get(env_var)
        if value:
            return value

    config_paths = [
        "config.json",
        os.path.expanduser("~/.openclaw/config.json"),
        os.path.expanduser("~/.claude/config.json"),
    ]
    for path in config_paths:
        if os.path.exists(path):
            try:
                with open(path) as f:
                    data = json.load(f)
                for key in ["zai_api_key", "glm_api_key", "api_key"]:
                    if data.get(key):
                        return data[key]
            except Exception:
                pass

    script_dir = os.path.dirname(os.path.abspath(__file__))
    skill_dir = os.path.dirname(script_dir)
    env_paths = [
        os.path.join(skill_dir, ".env"),
        ".env",
        os.path.expanduser("~/.env"),
    ]
    for path in env_paths:
        if os.path.exists(path):
            try:
                with open(path) as f:
                    for line in f:
                        line = line.strip()
                        for env_var in ["ZAI_API_KEY", "GLM_API_KEY"]:
                            if line.startswith(f"{env_var}="):
                                val = line.split("=", 1)[1].strip().strip('"')
                                if val:
                                    return val
            except Exception:
                pass

    return None


def load_glm_key() -> str:
    key = _load_key_from_env_and_configs()
    if not key:
        raise ValueError(
            "ZAI_API_KEY not found.\n"
            "Configure one of:\n"
            "  export ZAI_API_KEY=your-key\n"
            "  or add to ~/.openclaw/config.json: {\"zai_api_key\": \"your-key\"}\n"
            "Fallback key names still accepted: GLM_API_KEY / glm_api_key / api_key"
        )
    return key


def glm_cost_str(quality: str) -> str:
    cny = GLM_PRICE_HD_CNY if quality == "hd" else GLM_PRICE_STANDARD_CNY
    usd = cny * CNY_TO_USD
    return f"¥{cny:.2f} (~${usd:.4f})"


def generate_image_glm(
    prompt: str,
    size: str = "1088x1920",
    quality: str = "hd",
    watermark: bool = False,
    output_dir: str = "output",
) -> dict:
    api_key = load_glm_key()
    url = "https://open.bigmodel.cn/api/paas/v4/images/generations"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    body = {
        "model": "glm-image",
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "watermark_enabled": str(watermark).lower(),
    }

    response = requests.post(url, headers=headers, json=body, timeout=120)
    response.raise_for_status()
    data = response.json()

    if "data" not in data or not data["data"]:
        raise RuntimeError("No image returned from GLM API")

    image_url = data["data"][0]["url"]
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_prompt = re.sub(r'[\\/:*?"<>|]', "", prompt).replace(" ", "_")[:30]
    filename = f"{timestamp}_{safe_prompt}.png"
    filepath = os.path.join(output_dir, filename)

    img_response = requests.get(image_url, timeout=60)
    img_response.raise_for_status()
    with open(filepath, "wb") as f:
        f.write(img_response.content)

    return {
        "url": image_url,
        "local_path": filepath,
        "prompt": prompt,
        "quality": quality,
        "model": "glm-image",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate scrapbook-style image via Z.AI GLM-image")
    parser.add_argument("prompt", help="Image description")
    parser.add_argument(
        "--language",
        required=True,
        choices=list(SUPPORTED_LANGUAGES.keys()),
        help="Prompt language",
    )
    parser.add_argument("--size", default="1088x1920", help="Image size (default: 1088x1920)")
    parser.add_argument("--quality", default="hd", help="Image quality (default: hd)")
    parser.add_argument("--output", default="output", help="Output directory (default: output)")
    parser.add_argument("--watermark", action="store_true", help="Enable watermark")
    args = parser.parse_args()

    try:
        result = generate_image_glm(
            prompt=args.prompt,
            size=args.size,
            quality=args.quality,
            watermark=args.watermark,
            output_dir=args.output,
        )

        lang_label = SUPPORTED_LANGUAGES.get(args.language, args.language)
        print("Provider: zai")
        print("Model: glm-image")
        print(f"Language: {lang_label} ({args.language})")
        print(f"Image saved: {result['local_path']}")
        print(f"\nMarkdown URL:\n![{result['prompt']}]({result['url']})")
        print(f"\nLocal path: {result['local_path']}")
        print(f"\nCost: {glm_cost_str(result.get('quality', args.quality))}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
