# URL Shortener API

Production-ready URL shortener built using FastAPI, PostgreSQL, and Redis. This project demonstrates backend system design concepts including caching, expiry handling, analytics, and containerized deployment.

---

## Live Demo

https://your-app-name.onrender.com/docs

---

## Features

* Shorten long URLs into unique short links
* Redirect to original URL using short code
* Redis caching for fast lookups
* Expiry support for temporary links
* Click analytics tracking
* RESTful API with FastAPI
* Dockerized architecture for easy deployment

---

## Tech Stack

* Backend: FastAPI (Python)
* Database: PostgreSQL
* Cache: Redis
* ORM: SQLAlchemy
* Containerization: Docker & Docker Compose
* Deployment: Render

---

## Project Structure

```
url-shortener/
│
├── app/
│   ├── database/
│   ├── models/
│   ├── routes/
│   ├── schemas/
│   └── main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

---

## How It Works

1. User submits a long URL
2. System generates a unique short code
3. URL is stored in PostgreSQL
4. Redis caches frequently accessed URLs
5. On redirect:

   * Redis is checked first (fast)
   * If miss → PostgreSQL is queried
6. Expired URLs are automatically invalidated
7. Click count is tracked for analytics

---

## API Endpoints

### Create Short URL

POST /shorten

```
{
  "original_url": "https://example.com",
  "expiry_seconds": 60
}
```

---

### Redirect

GET /{short_code}

---

### Analytics

GET /stats/{short_code}

```
{
  "short_code": "abc123",
  "original_url": "https://example.com",
  "clicks": 10,
  "expiry_time": "2026-03-30T12:00:00"
}
```

---

## Running Locally

### Without Docker

```
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### With Docker

```
docker compose up --build
```

---

## Key Design Concepts

* Cache-aside pattern using Redis
* Service-based container communication
* Retry logic for service readiness
* Timezone-aware expiry handling
* Clean modular architecture

---

## Future Improvements

* User authentication
* Custom aliases for short URLs
* Rate limiting
* Frontend UI
* Monitoring and logging

---

## Author

Lalith Balaji
Python Developer | Data Engineer
Liverpool, UK

LinkedIn: https://linkedin.com/in/lalith-balaji
