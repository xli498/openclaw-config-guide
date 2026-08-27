# OpenClaw Configuration Guide

A controlled reference for configuring OpenClaw from real deployment experience. It is not a drop-in replacement configuration. Read the [scope and safety boundaries](./docs/00-%E9%80%82%E7%94%A8%E8%8C%83%E5%9B%B4%E4%B8%8E%E5%AE%89%E5%85%A8%E8%BE%B9%E7%95%8C.md) before changing a live instance.

## Contents

- [Quick Start](./docs/01-%E5%BF%AB%E9%80%9F%E5%90%AF%E5%8A%A8.md)
- [Model Configuration](./docs/02-%E6%A8%A1%E5%9E%8B%E9%85%8D%E7%BD%AE.md)
- [Channel Configuration](./docs/03-%E6%B8%A0%E9%81%93%E9%85%8D%E7%BD%AE.md)
- [Proxy and Network](./docs/04-%E4%BB%A3%E7%90%86%E7%BD%91%E7%BB%9C.md)
- [Troubleshooting](./docs/09-%E5%B8%B8%E8%A7%81%E9%97%AE%E9%A2%98%E6%8E%92%E9%94%99.md)
- [Compatibility Matrix](./docs/13-%E5%85%BC%E5%AE%B9%E6%80%A7%E7%9F%A9%E9%98%B5.md)

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
