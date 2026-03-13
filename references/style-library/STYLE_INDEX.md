# Style Library

Use these reference styles when the user wants a known visual treatment instead of a vague scrapbook prompt.

## Style 1: Board System

- File: `style-1-board-system.png`
- Look: 蓝色系统板 + 撕裂纸 + 手机界面 + 少量大字标题
- Best for: 讲流程、讲系统、讲工具链、讲排版规则
- Keywords: `蓝色系统板`, `版式统一`, `模块化`, `清晰结构`

## Style 2: Blue Poster

- File: `style-2-blue-poster.png`
- Look: 蓝色竖版海报，手机/界面做主视觉，贴少量便签
- Best for: 工具介绍、个人工作流、产品结构图
- Keywords: `竖版海报`, `大主视觉`, `少字`, `高质感`

## Style 3: Character Sticker

- File: `style-3-character-sticker.png`
- Look: 可爱角色贴纸 + 大图标 + 少量结论型文字
- Best for: 科普、类比、轻松一点的解释型文章
- Keywords: `角色贴纸`, `轻科普`, `卡通`, `结论提示`

## Style 4: Editorial Story

- File: `style-4-editorial-story.png`
- Look: 更像杂志插页或报道配图，情绪感更强
- Best for: 观点文、故事文、人物/人机关系类主题
- Keywords: `杂志感`, `叙事感`, `情绪`, `编辑感`

## Style 5: Bold Metaphor Scrapbook

- Files: `style-5-ai-makes-you-boring/sample-1.jpg`, `sample-2.png`, `sample-3.png`
- Look: 大标题撕纸 + 夸张比喻物件 + 贴纸人物 + 强结论句
- Best for: 观点文、批判性文章、强论点科普、需要“一眼看懂”的结论图
- Keywords: `粗标题`, `比喻`, `贴纸感`, `强观点`, `一图讲清`

## Prompting Rule

When the user says:

- `风格1` -> follow Style 1
- `风格2` -> follow Style 2
- `风格3` -> follow Style 3
- `风格4` -> follow Style 4
- `风格5` -> follow Style 5

If the user names no style:

- For WeChat technical articles, default to Style 2 or Style 1
- For explainer articles, prefer Style 3
- For opinion/story articles, prefer Style 4
- For strong-opinion or metaphor-heavy articles, prefer Style 5
