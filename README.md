# FastAPI REST API Template

Backend starter template for API-driven products with JWT authentication, CRUD endpoints, and PostgreSQL integration.

## Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- JWT authentication
- SQLite fallback for local demo

## Suggested Features

- User registration and login
- Access token generation
- Protected routes
- CRUD operations for a sample resource
- Database session management
- Environment-based settings

## Structure

- `app/main.py`: app bootstrap
- `app/core/config.py`: settings
- `app/core/security.py`: password hashing and JWT creation
- `app/db/session.py`: database session
- `app/models/`: SQLAlchemy models
- `app/api/routes/auth.py`: auth routes
- `app/api/routes/items.py`: CRUD routes
- `app/schemas/`: request and response models
- `app/services/`: business logic
- `requirements.txt`: dependencies
- `.env.example`: environment variable reference
- `Makefile`: shortcut commands for install and run
- `Dockerfile`: containerized demo setup

## Upwork Positioning

Use this project to show that you can deliver a clean API foundation for MVPs, admin systems, marketplaces, and internal tools.

## Quick Start

1. Create a virtual environment
2. Install dependencies from `requirements.txt`
3. Copy `.env.example` to `.env`
4. Run the app with `uvicorn app.main:app --reload`
5. Open `/docs` to present the API interface

Shortcut commands:
- `make install`
- `make run`

Docker demo:
- `docker build -t fastapi-template .`
- `docker run -p 8000:8000 fastapi-template`

## Demo Routes

- `GET /health`
- `POST /auth/register`
- `POST /auth/login`
- `POST /items/?owner_id=1`
- `GET /items/{item_id}`

## Demo Talking Points

- Show the `/health` endpoint first
- Register a user, then log in to generate a JWT token
- Show `/items` endpoints as CRUD examples
- Explain that `DATABASE_URL` can switch from SQLite to PostgreSQL without changing route structure
