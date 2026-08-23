# OriOS Lite

Lightweight orchestration and sandbox API for Ori.

## Deploy to Render

1. Open Render and choose **New → Web Service**.
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

8. Add an environment variable named `ORIOS_API_KEY` and generate a strong random value. Do not commit this secret to GitHub.

After deployment, test:

```text
https://YOUR-RENDER-SERVICE.onrender.com/health
```

The expected response is JSON with `status: ok`.

## API

Protected endpoints use:

```http
Authorization: Bearer YOUR_ORIOS_API_KEY
```

Create a workspace:

```http
POST /api/sandbox/workspaces
Content-Type: application/json
Authorization: Bearer YOUR_ORIOS_API_KEY

{"project_id":"ori-platform"}
```

List workspaces:

```http
GET /api/sandbox/workspaces
Authorization: Bearer YOUR_ORIOS_API_KEY
```

## Architecture

```text
Vercel Ori Platform
        |
        | HTTPS + Bearer token
        v
OriOS Lite API (Render)
        |
        v
Sandbox Manager
        |
        v
Isolated sandbox runtime
```

The current workspace endpoints are a deployment-ready API foundation. Runtime provisioning, persistent storage, task execution, logs, snapshots, and previews will be added behind the same API boundary.
