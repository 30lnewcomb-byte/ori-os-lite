from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="OriOS Lite API", version="0.1.0")


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


class SandboxRequest(BaseModel):
    project_id: str = Field(min_length=1, max_length=128)


workspaces: dict[str, dict[str, str]] = {}


def require_api_key(authorization: str | None) -> None:
    expected = os.getenv("ORIOS_API_KEY")
    if expected and authorization != f"Bearer {expected}":
        raise HTTPException(status_code=401, detail="Invalid or missing API key")


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="orios-lite", version="0.1.0")


@app.get("/")
def root() -> dict[str, str]:
    return {"service": "OriOS Lite", "status": "online", "version": "0.1.0"}


@app.get("/api/sandbox/workspaces")
def list_workspaces(authorization: str | None = Header(default=None)) -> list[dict[str, str]]:
    require_api_key(authorization)
    return list(workspaces.values())


@app.post("/api/sandbox/workspaces", status_code=201)
def create_workspace(
    request: SandboxRequest,
    authorization: str | None = Header(default=None),
) -> dict[str, Any]:
    require_api_key(authorization)
    workspace_id = f"ws-{len(workspaces) + 1:04d}"
    workspace = {
        "workspace_id": workspace_id,
        "project_id": request.project_id,
        "status": "ready",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    workspaces[workspace_id] = workspace
    return workspace
