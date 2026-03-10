---
name: article-illustrator
description: Insert scrapbook-style illustrations into articles using Z.AI GLM-image. Use when the user wants to add images to an article, create illustrated content, or requests "illustrate this article", "add images to this article", "generate pictures for this post", "insert illustrations".
---

# Scrapbook-Style Illustration Inserter

Transform articles into illustrated markdown by generating hand-crafted scrapbook-style images and inserting them at logical break points.

> **Attribution:** Based on [glm-image](https://github.com/ViffyGwaanl/glm-image) by ViffyGwaanl (MIT License).

## Setup

This skill uses **Z.AI API key only** and always calls **`glm-image`**.

Configure one of:
- `export ZAI_API_KEY="your-key"`
- Add `"zai_api_key": "your-key"` to `~/.openclaw/config.json`

Backward-compatible fallback names are still accepted by the bundled script:
- `GLM_API_KEY`
- `glm_api_key`
- `api_key`

## Inputs

- **article**: The full article text (markdown or plain text)
- **image_count** (optional): Number of images to generate, 2–5 (default: 3)
- **orientation** (optional): `portrait` (1088x1920, default) or `landscape` (1920x1088)
- **language** (required): Language for text in generated images — `zh`, `en`, `ja`, `ko`, `fr`, `de`, `es`. Always ask the user; never default or infer.

## Workflow

### Step 0: Check API Key

If `ZAI_API_KEY` is not configured (or compatible fallback key names are missing), stop and tell the user how to configure it. Do not proceed without a valid key.

### Step 1: Validate Input

Before generating any images:
- Confirm article is at least 200 words. If shorter, warn user: "Article may be too short for meaningful illustration — proceed anyway?"
- Count major sections or topic transitions (H2 headings, paragraph breaks). This determines insertion points.
- Ask the user which language to use for image text. Never infer from the article language.

### Step 2: Generate Image Prompts

Read the scrapbook system prompt from `references/scrapbook-prompt.md`.

Using that prompt, analyze the article and output a JSON plan:

```json
{
  "project_title": "Article title — Scrapbook Style",
  "style": "Physical Mixed-Media Scrapbook",
  "total_images": 3,
  "images": [
    {
      "image_id": 1,
      "title": "Image caption",
      "description": "300-500 character visual description in scrapbook style...",
      "insert_after": "Exact sentence or heading after which to insert the image"
    }
  ]
}
```

Target 1 image per 300–400 words of article content.

### Step 3: Generate All Images in Parallel

Launch all image generations simultaneously.

```bash
python3 scripts/generate.py "<description_1>" --language <lang> --size 1088x1920 &
python3 scripts/generate.py "<description_2>" --language <lang> --size 1088x1920 &
python3 scripts/generate.py "<description_3>" --language <lang> --size 1088x1920 &
wait
```

The bundled script always calls `glm-image` via Z.AI / BigModel-compatible API.

On failure: if generation fails for one image, log the error and continue with remaining images. Do not abort the entire run.

### Step 4: Compose Final Markdown

Insert each image after its designated `insert_after` anchor:

```markdown
![Image caption](image_url)
```

If the `insert_after` anchor is not found verbatim, insert at the nearest paragraph break.

## Output Format

Return the complete markdown article with:
1. All original article text preserved exactly
2. Generated images inserted at logical break points
3. Captions from the JSON plan
4. A summary line at the end: `<!-- Illustrated: N images generated, M failed, total cost: $X.XX -->`

## Edge Cases

- **Short article (<200 words)**: Warn and confirm before proceeding
- **Generation failure**: Log error inline, continue with other images — do not abort
- **Anchor not found**: Insert at nearest paragraph break instead
- **No API key**: Surface error immediately with setup instructions
- **All images fail**: Return original article unchanged with error summary
