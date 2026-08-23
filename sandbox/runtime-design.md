# Sandbox Runtime Plan

The sandbox is Ori's development workshop. It must never become an unrestricted remote shell.

## Runtime boundary

```text
OriOS Lite API
      |
      v
Sandbox Manager
      |
      v
Runtime Adapter
      |
      v
Dedicated isolated container/VM
      |
      +-- workspace filesystem
      +-- process limits
      +-- CPU/memory limits
      +-- network policy
      +-- execution timeout
      +-- task logs
```

## v0.1 safety posture

- Workspace paths are resolved and prevented from escaping the workspace root.
- Command execution remains disabled until an isolated runtime is deployed.
- When enabled, commands must pass an explicit allowlist.
- The sandbox receives only the workspace it needs.
- Secrets from the OriOS Lite host are not mounted into the workspace.
- Tasks must have timeouts and resource limits.
- Network access should be disabled by default and explicitly enabled per task when required.

## Implementation sequence

1. Keep the API and workspace model provider-neutral.
2. Add a runtime adapter interface.
3. Run the adapter inside a dedicated sandbox container/VM.
4. Add resource and timeout enforcement.
5. Add structured stdout/stderr/task events.
6. Add Git operations through the sandbox boundary.
7. Add preview artifact handling.
8. Add snapshots/restore.

The Render service is the control plane. It should not directly execute arbitrary model-generated commands in the service process.
