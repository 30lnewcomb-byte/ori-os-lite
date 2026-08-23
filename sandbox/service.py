from __future__ import annotations

import asyncio
import os
import uuid
from pathlib import Path

from .models import TaskRequest, TaskResult, TaskStatus, Workspace, WorkspaceStatus


class SandboxService:
    """Manage project workspaces without exposing the host filesystem.

    This first runtime deliberately provides workspace management and a safe
    execution boundary. The production Render deployment should place this
    service behind a dedicated isolated runtime/container before arbitrary
    model-generated commands are enabled.
    """

    def __init__(self, root: str | None = None) -> None:
        self.root = Path(root or os.getenv("SANDBOX_ROOT", "/tmp/orios-sandbox")).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.workspaces: dict[str, Workspace] = {}

    def create_workspace(self, project_id: str) -> Workspace:
        workspace_id = f"ws-{uuid.uuid4().hex[:12]}"
        path = (self.root / workspace_id).resolve()
        path.mkdir(parents=True, exist_ok=False)
        workspace = Workspace(workspace_id=workspace_id, project_id=project_id, path=str(path))
        self.workspaces[workspace_id] = workspace
        return workspace

    def get_workspace(self, workspace_id: str) -> Workspace:
        workspace = self.workspaces.get(workspace_id)
        if workspace is None:
            raise KeyError(workspace_id)
        return workspace

    def _safe_path(self, workspace: Workspace, relative_path: str) -> Path:
        candidate = (Path(workspace.path) / relative_path).resolve()
        workspace_root = Path(workspace.path).resolve()
        if candidate != workspace_root and workspace_root not in candidate.parents:
            raise ValueError("Path escapes sandbox workspace")
        return candidate

    def read_file(self, workspace_id: str, relative_path: str) -> str:
        workspace = self.get_workspace(workspace_id)
        return self._safe_path(workspace, relative_path).read_text(encoding="utf-8")

    def write_file(self, workspace_id: str, relative_path: str, content: str) -> None:
        workspace = self.get_workspace(workspace_id)
        path = self._safe_path(workspace, relative_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    async def run_task(self, request: TaskRequest) -> TaskResult:
        """Placeholder execution boundary.

        Arbitrary command execution is intentionally not enabled yet. This
        prevents an internet-facing Render service from becoming an unrestricted
        remote shell while the isolated runtime is being implemented.
        """
        self.get_workspace(request.workspace_id)
        await asyncio.sleep(0)
        return TaskResult(
            task_id=f"task-{uuid.uuid4().hex[:12]}",
            workspace_id=request.workspace_id,
            status=TaskStatus.FAILED,
            stderr="Sandbox runtime execution is not enabled in v0.1.0.",
            exit_code=None,
        )
