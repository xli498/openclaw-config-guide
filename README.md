# OpenClaw 配置指南

基于 OpenClaw 真实部署经验的配置指南。覆盖从零开始的完整配置流程。

## 目录

| 文件 | 内容 | 适合谁 |
|:-----|:-----|:-------|
| [01-快速启动.md](./docs/01-快速启动.md) | 从零到能聊天 | 刚装好 OpenClaw 的人 |
| [02-模型配置.md](./docs/02-模型配置.md) | DeepSeek / OpenRouter / MiMo / 小艺 | 想省钱又想用好模型的人 |
| [03-渠道配置.md](./docs/03-渠道配置.md) | 微信 / QQ / 小艺渠道 | 想让 AI 接入聊天工具的人 |
| [04-代理网络.md](./docs/04-代理网络.md) | Mihomo / 代理路由 / 隧道 | 在国内需要访问境外 API 的人 |
| [05-代理网络实战.md](./docs/05-代理网络实战.md) | Mihomo 配置 / env-proxy / Header 编码 / 看门狗 | 需要深入代理配置的人 |
| [06-常见问题排错.md](./docs/06-常见问题排错.md) | 微信重复回复 / 插件去重 / send_file_to_user bug / Compaction / QQ Bot / TTS | 遇到问题的人 |
| [07-多渠道配置实战.md](./docs/07-多渠道配置实战.md) | 微信 + QQ Bot 双渠道 / 图片服务 / TTS 代理 | 需要多渠道部署的人 |

## 30 秒快速启动

```bash
# 1. 安装 OpenClaw
npm install -g openclaw

# 2. 初始化
openclaw init

# 3. 配置 API Key（以 DeepSeek 为例）
# 编辑 ~/.openclaw/openclaw.yaml
# 或通过 openclaw config set 设置

# 4. 启动
openclaw gateway start

# 5. 验证
openclaw channel list
```

## 核心理念

### 模型选择

| 场景 | 推荐模型 | 月成本估算 |
|:-----|:---------|:----------|
| 日常对话 | DeepSeek V4 Flash | ~¥5 |
| 复杂推理 | DeepSeek V4 Pro | ~¥20 |
| 代码/多模态 | Claude Sonnet 4.6 (OpenRouter) | ~$15 |
| 手机操控 | MiMo V2.5 Pro | 免费 |

### 渠道配置

- **微信** — 最常用，需要配置 weixin-bridge
- **QQ Bot** — 官方 API，appId 1903992323
- **小艺渠道** — 华为原生，开箱即用

### 记忆管理

- 记忆三层架构：L1 痕迹 → L2 模式 → L3 技能
- KAIROS 心跳 — 会话启动时自动扫描
- AutoDream 记忆整理 — 三重门控：时间(12h) + 量级(5条) + 质量(>0.3)
- AutoMemory 自动记忆 — 深度对话自动提取

## 技术架构

```
┌─────────────────────────────────────────┐
│              OpenClaw Gateway            │
├──────────┬──────────┬───────────────────┤
│ 渠道层   │ 模型层   │ 工具层            │
│          │          │                   │
│ 微信 ◄───┤ DeepSeek ├─► Skills          │
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

## 实战数据

基于持续运行的 OpenClaw 实例：

| 指标 | 数据 |
|:-----|:-----|
| 已安装 Skills | 123+ |
| 已配置渠道 | 3 个（微信/QQ/小艺） |
| 已接入模型 | 8 个（DeepSeek/MiMo/Claude/GPT/MiniMax） |
| 月均成本 | ~¥20（主要用 DeepSeek） |

## 贡献

这不是官方文档，是实战经验。每条内容都是踩坑踩出来的。如果你也踩了坑，欢迎 PR。

## 许可证

MIT
