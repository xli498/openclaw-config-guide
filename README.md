# 🦞 OpenClaw 新手生存指南

> *"如果你需要一份说明书才能用它，那说明它还不够好。但如果你连说明书都没有，那说明你完了。"*
> — **Elon Musk**（如果他来搭 AI Agent 的话）

---

## 这是什么？

一份**经过实战验证**的 OpenClaw 配置指南。不是官方文档的复读机，而是一个在真实环境里跑了两周、踩了无数坑之后总结出来的**生存手册**。

如果你刚装好 OpenClaw，对着 `openclaw.json` 一脸懵逼——恭喜你，来对地方了。

---

## 📋 目录

| 文件 | 内容 | 适合谁 |
|:-----|:-----|:-------|
| [01-快速启动.md](./docs/01-快速启动.md) | 从零到能聊天 | 刚装好 OpenClaw 的人 |
| [02-模型配置.md](./docs/02-模型配置.md) | DeepSeek / OpenRouter / MiMo / 小艺 | 想省钱又想用好模型的人 |
| [03-渠道配置.md](./docs/03-渠道配置.md) | 微信 / QQ / 小艺渠道 | 想让 AI 接入聊天工具的人 |
| [04-代理网络.md](./docs/04-代理网络.md) | Mihomo / 代理路由 / 隧道 | 在国内需要访问境外 API 的人 |
| [05-技能系统.md](./docs/05-技能系统.md) | Skills 安装 / 管理 / 推荐 | 想让 AI 能力暴增的人 |
| [06-记忆与进化.md](./docs/06-记忆与进化.md) | 记忆管理 / 自主进化 / KAIROS | 想让 AI 记住你的人 |
| [07-安全配置.md](./docs/07-安全配置.md) | 安全策略 / 脱敏 / 权限控制 | 所有人（必读） |
| [08-踩坑实录.md](./docs/08-踩坑实录.md) | 真实踩坑 + 解决方案 | 遇到问题的人 |
| [09-配置模板.md](./docs/09-配置模板.md) | 可直接复制的配置文件 | 想快速上手的人 |

---

## 🚀 30 秒快速启动

```bash
# 1. 安装 OpenClaw
npm install -g openclaw

# 2. 初始化
openclaw init

# 3. 配置你的 API Key（以 DeepSeek 为例）
# 编辑 ~/.openclaw/openclaw.json，在 models.providers 里添加：
# "deepseek": {
#   "apiKey": "sk-your-key-here",
#   "baseUrl": "https://api.deepseek.com",
#   "api": "openai-completions"
# }

# 4. 启动
openclaw gateway start

# 5. 打开控制面板
open http://localhost:18789
```

就这么简单。5 个命令，你的 AI 就活了。

---

## ⚡ 核心理念

### 1. 模型选择：不是越贵越好

| 场景 | 推荐模型 | 月成本估算 |
|:-----|:---------|:----------|
| 日常对话 | DeepSeek V4 Flash | ~¥5 |
| 复杂推理 | DeepSeek V4 Pro | ~¥20 |
| 代码/多模态 | Claude Sonnet 4.6 (OpenRouter) | ~$15 |
| 手机操控 | MiMo V2.5 Pro | 免费 |

### 2. 渠道选择：一个都不能少

- **微信** — 最常用，但需要登录网页版
- **QQ Bot** — 官方 API，稳定但配置复杂
- **小艺渠道** — 华为原生，开箱即用

### 3. 记忆管理：这才是核心

普通 AI 每次对话都是白痴。配置好记忆系统后，它会：
- 记住你的名字、偏好、习惯
- 从错误中学习，不再重复踩坑
- 空闲时自动整理记忆（AutoDream）

---

## 🏗️ 技术架构

```
┌─────────────────────────────────────────┐
│              OpenClaw Gateway            │
├──────────┬──────────┬───────────────────┤
│ 渠道层   │ 模型层   │ 工具层            │
│          │          │                   │
│ 微信 ◄───┤ DeepSeek ├─► Skills (123+)   │
│ QQ   ◄───┤ MiMo     ├─► Browser         │
│ 小艺 ◄───┤ Claude   ├─► Memory          │
│          │ GPT-4o   ├─► File System     │
├──────────┴──────────┴───────────────────┤
│           记忆层 (L1/L2/L3)              │
│  traces → patterns → executable models  │
├─────────────────────────────────────────┤
│           安全层 (Fail-closed)           │
│  Secret Guardian / Execution Validator   │
└─────────────────────────────────────────┘
```

---

## 📊 我们的实战数据

经过两周高强度使用，以下数据供参考：

| 指标 | 数据 |
|:-----|:-----|
| 已安装 Skills | 123+ |
| 已配置渠道 | 3 个（微信/QQ/小艺） |
| 已接入模型 | 8 个（DeepSeek/MiMo/Claude/GPT/MiniMax） |
| 记忆主题文件 | 8 个 |
| 踩坑记录 | 7 条（全部已解决） |
| 自主进化能力 | 6 项（KAIROS/AutoDream/AutoMemory/Context Engineering/情绪感知/Degenerate Loop 检测） |
| 月均成本 | ~¥20（主要用 DeepSeek） |

---

## 🤝 贡献

这不是官方文档，是实战经验。如果你也踩了坑，欢迎 PR。

---

## 📜 许可证

MIT — 用就完了。

---

*"第一性原理：不要问'OpenClaw 怎么配置'，问'我要解决什么问题'。"*
