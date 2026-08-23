from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="OriOS Lite API", version="0.1.0")


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


class SandboxRequest(BaseModel):
    project_id: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service="orios-lite", version="0.1.0")


@app.get("/")
def root() -> dict[str, str]:
    return {"service": "OriOS Lite", "status": "online"}


@app.post("/api/sandbox/workspaces")
def create_workspace(request: SandboxRequest) -> dict[str, str]:
    # Runtime provisioning will be implemented behind SandboxProvider.
    return {
        "status": "accepted",
        "project_id": request.project_id,
        "message": "Sandbox provisioning endpoint is ready for the runtime provider.",
    }
