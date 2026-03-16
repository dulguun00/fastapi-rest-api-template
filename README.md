# FastAPI REST API Template

Production-style FastAPI backend starter with JWT authentication, CRUD endpoints, and PostgreSQL-ready architecture.

This repository is designed as a portfolio project for API-driven applications such as startup MVPs, internal tools, SaaS backends, and client portals. It demonstrates how to organize a backend in a way that is clean, extendable, and aligned with real freelance requirements.

Portfolio cover reference:
`../../assets/fastapi-cover.svg`

## Portfolio Highlights

- JWT-based authentication flow
- Modular CRUD route structure
- SQLAlchemy models and service layer separation
- SQLite local demo with PostgreSQL-ready configuration
- Docker and Makefile support for faster setup

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

## API Demo Flow

1. Register a user through `POST /auth/register`
2. Log in through `POST /auth/login`
3. Create an item through `POST /items/?owner_id=1`
4. Fetch the item through `GET /items/{item_id}`
5. Verify service health through `GET /health`

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

## Why This Project Works In A Portfolio

Clients looking for backend help usually want more than a single endpoint. This project shows application structure, security basics, persistence, and code organization in a way that is easy to discuss during technical screening or proposal conversations.
