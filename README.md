# URL Shortener

A full-stack URL shortener with a REST API backend, React frontend, and PostgreSQL database. Deployed on Render with automated CI/CD via GitHub Actions.

## Live Demo
- **Frontend:** [your-frontend-url.onrender.com]
- **API:** [your-backend-url.onrender.com]

## Tech Stack
- **Backend:** Node.js, Express, PostgreSQL
- **Frontend:** React
- **Database:** PostgreSQL (Render)
- **Deployment:** Render
- **CI/CD:** GitHub Actions

## Features
- Shorten long URLs to compact links
- Redirect short URLs to original destinations
- Track click counts per URL
- REST API with full CRUD support

## Local Setup

**Prerequisites:** Node.js, PostgreSQL, Docker (optional)

```bash
# Clone the repo
git clone https://github.com/isha-1686/url-shortener.git
cd url-shortener

# Backend
cd backend
cp .env.example .env      # add your DATABASE_URL
npm install
npm start

# Frontend (new terminal)
cd frontend
npm install
npm start
```

**With Docker:**
```bash
docker-compose up
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/shorten` | Create short URL |
| GET | `/:code` | Redirect to original URL |
| GET | `/api/urls` | List all URLs |
| DELETE | `/api/urls/:id` | Delete a URL |

## CI/CD
Every push to `main` triggers a GitHub Actions pipeline that builds the project and runs a health check against the live backend.