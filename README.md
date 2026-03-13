# article-illustrator

Transform articles into richly illustrated markdown using **hand-crafted scrapbook-style images** generated via **Z.AI GLM-image**.

**Attribution:** Based on [glm-image](https://github.com/ViffyGwaanl/glm-image) by ViffyGwaanl (MIT License).

## Requirements

- Python 3
- `requests`
- `ZAI_API_KEY` set in environment or config
  - fallback names still accepted by the script: `GLM_API_KEY`, `glm_api_key`, `api_key`

## What it does

1. Reads an article
2. Plans 2–5 scrapbook-style illustrations
3. Generates each image via **Z.AI GLM-image only**
4. Returns the article with images embedded at logical insertion points

## Style References

The skill now includes a local sample library under `references/style-library/`.

You can ask for:
- `风格1` / `style 1` — Board System
- `风格2` / `style 2` — Blue Poster
- `风格3` / `style 3` — Character Sticker
- `风格4` / `style 4` — Editorial Story
- `风格5` / `style 5` — Bold Metaphor Scrapbook

For WeChat technical articles, `风格2` and `风格1` are usually the safest defaults.

## Notes

- No OpenRouter support
- No model switching
- Always uses `glm-image`
