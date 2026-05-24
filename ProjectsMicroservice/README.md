# Projects Microservice

A Django REST Framework microservice that exposes project data from Mockend. Part of the __init__to_win_it suite of microservices.

---

## Endpoints

- `GET /api/projects/` — List all projects
- `GET /api/projects/<id>/` — Retrieve a project by ID
- `GET /api/docs/` — Swagger 
- `GET /api/schema/` — OpenAPI 3 JSON schema
- `GET /api/redoc/` — ReDoc UI

### Example Response

```json
{
  "id": 101,
  "name": "Jira Board Clone",
  "key": "JBC",
  "leadProfileId": 1
}
```

---

## Running with Docker

From the root `__init__to_win_it` directory:

```bash
docker compose up --build --watch
```

The service runs on **http://localhost:8001**.

---

## Running locally

```bash
cd ProjectsMicroservice
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

Project data is defined in projects.yml and served by Mockend at:

```
https://mockend.com/api/angeletapersaud/__init__to_win_it/projects
```
