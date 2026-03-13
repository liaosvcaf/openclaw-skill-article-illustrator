# Style Library

Use these reference styles when the user wants a known visual treatment instead of a vague scrapbook prompt.

Quick overview:
- Gallery page: `STYLE_GALLERY.md`
- Contact sheet: `style-gallery.png`

## Style 1: Board System

- File: `style-1-board-system.png`
- Look: 组织结构板 + 任务角色分层 + 纸张拼贴，像“数字公司/任务看板”的主视觉
- Best for: 讲系统架构、角色分工、组织结构、agent 协同
- Keywords: `组织结构`, `任务看板`, `角色分层`, `系统板`

## Style 2: Blue Poster

- File: `style-2-blue-poster.png`
- Look: 强蓝色竖版海报，像“MISSION CONTROL”这种封面级主视觉，机器人和控制台很抓眼
- Best for: 工具介绍、封面图、任务指挥中心、主视觉型技术文章
- Keywords: `蓝色海报`, `主视觉`, `任务指挥中心`, `封面感`

## Style 3: Character Sticker

- File: `style-3-character-sticker.png`
- Look: 手绘小人 + 彩色便签 + 轻松拼贴感，可爱但不幼稚，适合讲思维转变
- Best for: 科普、成长型主题、轻松解释、给普通读者看的文章
- Keywords: `手绘小人`, `便签`, `成长型`, `轻科普`

## Style 4: Editorial Story

- File: `style-4-editorial-story.png`
- Look: 更像公众号观点文里的故事型海报，贴纸、对白、人物状态和“先试试看”的情绪很强
- Best for: 观点文、劝服型文章、叙事性技术文章、带一点情绪推进的内容
- Keywords: `叙事感`, `观点文`, `先试试看`, `故事型海报`

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
