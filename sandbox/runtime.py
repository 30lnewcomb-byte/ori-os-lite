from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class RuntimeLimits:
    timeout_seconds: int = 60
    memory_mb: int = 512
    cpu_limit: float = 1.0
    network_enabled: bool = False


class SandboxRuntime(Protocol):
    """Execution boundary implemented by an isolated runtime backend."""

    def create(self, workspace_path: str, limits: RuntimeLimits) -> str: ...

    def execute(self, runtime_id: str, command: list[str]) -> tuple[int, str, str]: ...

    def stop(self, runtime_id: str) -> None: ...

    def destroy(self, runtime_id: str) -> None: ...
