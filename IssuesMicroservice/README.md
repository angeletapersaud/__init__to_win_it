# Issues Microservice

A Django REST Framework microservice that exposes issue data from Mockend. Part of the __init__to_win_it suite of microservices.

---

## Endpoints

- `GET /api/issues/` — List all issues
- `GET /api/issues/<id>/` — Retrieve an issue by ID
- `GET /api/docs/` — Swagger
- `GET /api/schema/` — OpenAPI 3 JSON schema
- `GET /api/redoc/` — ReDoc UI

### Example Response

```json
{
  "id": 5001,
  "projectId": 101,
  "assigneeProfileId": 1,
  "summary": "Build board layout",
  "status": "To Do",
  "priority": "High"
}
```

---

## Running with Docker

From the root `__init__to_win_it` directory:

```bash
docker compose up --build --watch
```

The service runs on **http://localhost:8002**.

---

## Running locally

```bash
cd IssuesMicroservice
python -m venv venv
source venv/bin/activate      
pip install -r requirements.txt
cp .env.example .env          
python manage.py runserver
```

The service runs on **http://localhost:8000**.

---

## Configuration

Copy `.env.example` to `.env` and set variables:

---

## Data Source

Issue data is defined in issues.yml and served by Mockend at:

```
https://mockend.com/api/angeletapersaud/__init__to_win_it/issues
```

