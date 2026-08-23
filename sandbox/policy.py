from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CommandPolicy:
    """Explicit allowlist for development commands.

    This is intentionally conservative. Expand it only after the runtime is
    isolated in its own container/VM with CPU, memory, filesystem, process,
    and network limits.
    """

    allowed_programs: frozenset[str] = frozenset({
        "python",
        "python3",
        "node",
        "npm",
        "git",
    })

    def validate(self, command: list[str]) -> None:
        if not command:
            raise ValueError("Command cannot be empty")
        if len(command) > 32:
            raise ValueError("Command is too long")
        program = command[0].rsplit("/", 1)[-1].rsplit("\\", 1)[-1]
        if program not in self.allowed_programs:
            raise PermissionError(f"Program is not allowed: {program}")
