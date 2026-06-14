# URL Shortener

A full-stack URL shortener with a FastAPI backend, React frontend, and PostgreSQL database. Deployed on Render with Docker and automated CI/CD via GitHub Actions.

## Live Demo
- **Frontend:** https://url-shortener-1-ww94.onrender.com
- **API:** https://url-shortener-v5xu.onrender.com

> Note: Hosted on Render's free tier — first request may take up to 50 seconds to wake the server.

## Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Python, FastAPI |
| Frontend | React, Vite |
| Database | PostgreSQL |
| Containerization | Docker, Docker Compose |
| Deployment | Render |
| CI/CD | GitHub Actions |

## Features
- Shorten long URLs to compact links
- Redirect short links to original URLs
- Dockerized for consistent local and production environments
- Automated CI pipeline validates every push to main

## Local Setup

**Prerequisites:** Python 3.11+, Node.js 20+, Docker (optional)

### Without Docker

```bash
git clone https://github.com/isha-1686/url-shortener.git
cd url-shortener

# Backend
cd backend
pip install -r requirements.txt
python main.py

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

### With Docker

```bash
docker-compose up
```

## CI/CD Pipeline

Every push to `main` triggers a GitHub Actions workflow that:
1. Installs Python dependencies and validates the backend
2. Installs Node.js dependencies and builds the React frontend

## Project Structure

```
url-shortener/
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
├── docker-compose.yml
└── .github/
    └── workflows/
        └── deploy.yml
```