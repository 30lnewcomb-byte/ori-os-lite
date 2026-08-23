# Ori Sandbox

The sandbox is Ori's development workshop.

It provides a controlled workspace where Ori can eventually create files, edit projects, run approved development commands, test code, use Git, and produce build/preview artifacts.

## Architecture

```text
OriOS Lite API
      |
      v
Sandbox Manager
      |
      v
SandboxRuntime
      |
      v
Isolated runtime
      |
      +-- workspace
      +-- CPU/memory limits
      +-- timeout
      +-- network policy
      +-- task output
```

`SandboxRuntime` is intentionally an interface. The control plane does not know whether the eventual implementation uses a container, microVM, or another isolated runtime.

## Current state

- Workspace creation/read/write: implemented.
- Workspace path escape protection: implemented.
- Runtime contract: implemented.
- Command policy: implemented as a conservative allowlist.
- Arbitrary execution: **disabled until the isolated runtime is wired in**.

## Why this separation matters

The Render service should orchestrate sandboxes; it should not execute untrusted model-generated commands directly inside the API process. The runtime must enforce filesystem, process, CPU, memory, timeout, and network boundaries.
