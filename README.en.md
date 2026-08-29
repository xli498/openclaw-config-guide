# OpenClaw Configuration Guide

A controlled reference for configuring OpenClaw from real deployment experience. It is not a drop-in replacement configuration. Read the [scope and safety boundaries](./docs/00-适用范围与安全边界.md) before changing a live instance.

## Contents

- [Quick Start](./docs/01-快速启动.md)
- [Model Configuration](./docs/02-模型配置.md)
- [Channel Configuration](./docs/03-渠道配置.md)
- [Proxy and Network](./docs/04-代理网络.md)
- [Troubleshooting](./docs/09-常见问题排错.md)
- [Compatibility Matrix](./docs/13-兼容性矩阵.md)

## Safety principles

- Inspect the current version and official schema before editing configuration.
- Make the smallest possible change; do not overwrite the whole configuration.
- Never commit API keys, private prompts, user data, private endpoints, or sensitive payloads.
- Verify the running state after a change and keep a rollback path.
- Treat examples as deployment-specific references, not universal defaults.

## Quick start

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
openclaw setup
openclaw status
```

Then add only the provider or channel fields you actually need, using the schema for the installed OpenClaw version. Run a minimal verification before considering a reload or restart.

This repository is community-maintained field documentation, not official OpenClaw documentation. Version-sensitive claims should be checked against the current official documentation.
