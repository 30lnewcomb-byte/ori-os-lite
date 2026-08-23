from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum

from pydantic import BaseModel, Field


class WorkspaceStatus(StrEnum):
    READY = "ready"
    BUSY = "busy"
    STOPPED = "stopped"


class TaskStatus(StrEnum):
    QUEUED = "queued"
    RUNNING = "running"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


class Workspace(BaseModel):
    workspace_id: str
    project_id: str
    path: str
    status: WorkspaceStatus = WorkspaceStatus.READY
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class TaskRequest(BaseModel):
    workspace_id: str
    command: list[str] = Field(min_length=1, max_length=32)


class TaskResult(BaseModel):
    task_id: str
    workspace_id: str
    status: TaskStatus
    stdout: str = ""
    stderr: str = ""
    exit_code: int | None = None
