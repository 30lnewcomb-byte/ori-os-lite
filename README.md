# OriOS Lite

Lightweight orchestration and sandbox API for Ori. The first hosted target is Render, while the Ori web application remains on Vercel.

## Deploy to Render

1. Open Render and choose **New → Web Service** (or deploy the repository as a Blueprint so Render can read `render.yaml`).
2. Connect the GitHub repository `30lnewcomb-byte/ori-os-lite`.
3. Use the repository root as the service root.
4. Runtime: **Python 3**.
5. Build command:

```bash
pip install -r requirements.txt
```

6. Start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

7. Health check path:

```text
/health
```

8. In Render **Environment**, add `ORIOS_API_KEY` and set it to a long random secret. Do not commit this value to GitHub.

9. Deploy. After deployment, test:

```text
https://YOUR-RENDER-SERVICE.onrender.com/health
```

The expected response contains `status: ok`.

## API authentication

`/health` is intentionally public so Render can monitor the service. Sandbox endpoints require:

```http
Authorization: Bearer YOUR_ORIOS_API_KEY
```

If `ORIOS_API_KEY` is missing, protected sandbox endpoints fail closed with a server configuration error instead of silently running without authentication.

## API

- `GET /` — service information
- `GET /health` — Render health check
- `GET /api/sandbox/workspaces` — list workspace records
- `POST /api/sandbox/workspaces` — create a workspace record

Create a workspace:

```http
POST /api/sandbox/workspaces
Content-Type: application/json
Authorization: Bearer YOUR_ORIOS_API_KEY

{"project_id":"ori-platform"}
```

## Architecture

```text
Vercel Ori Platform
        |
        | HTTPS + server-side Bearer token
        v
OriOS Lite API (Render)
        |
        v
Sandbox Manager
        |
        v
Isolated sandbox runtime
```

The current workspace endpoints are the deployment/API foundation. Runtime provisioning, persistent storage, task execution, logs, snapshots, and previews will be added behind the same API boundary.
