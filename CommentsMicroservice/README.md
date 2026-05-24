# Comments Microservice

A Django REST Framework microservice that exposes comment data from Mockend. Part of the __init__to_win_it suite of microservices.

---

## Endpoints

- `GET /api/comments/` — List all comments
- `GET /api/comments/<id>/` — Retrieve a comment by ID
- `GET /api/docs/` — Swagger
- `GET /api/schema/` — OpenAPI 3 JSON schema
- `GET /api/redoc/` — ReDoc UI

### Example Response

```json
{
  "id": 9001,
  "issueId": 5001,
  "profileId": 2,
  "message": "Looks good so far."
}
```

---

## Running with Docker

From the root `__init__to_win_it` directory:

```bash
docker compose up --build --watch
```

The service runs on **http://localhost:8003**.

---

## Running locally

```bash
cd CommentsMicroservice
python -m venv venv
source venv/bin/activate   
pip install -r requirements.txt
cp .env.example .env
python manage.py runserver
```
