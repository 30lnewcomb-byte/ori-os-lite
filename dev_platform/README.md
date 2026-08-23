# Ori Developer Platform

The Ori Developer Platform is the developer-facing layer around Ori. It is intended to provide a stable API, projects, tools, events, authentication, documentation, and eventually SDKs.

## Current foundation

- Project model
- API-key metadata model (no secrets stored in source)
- Tool registration model
- Platform event model
- Project-aware architecture

## Planned platform surface

```text
Ori Developer Platform
├── API
├── Authentication
├── Projects
├── Tools
├── Models
├── Events / Logs
├── Documentation
├── SDKs
└── Console
```

## Design principle

Ori should be able to use the same platform that developers use. The platform should expose stable interfaces instead of tying application code directly to individual infrastructure providers.

## Not connected yet

This repository does not currently provision API keys, connect external accounts, publish SDK packages, or expose a public developer API. Those are later implementation steps.
