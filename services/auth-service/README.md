# Auth Service

## Overview

Production-grade authentication service for OpenLearn AI with:

- ✅ JWT token-based authentication
- ✅ OAuth integration (Google, Microsoft)
- ✅ COPPA compliance (age gating, parental consent)
- ✅ Rate limiting
- ✅ Session management
- ✅ Password hashing with bcrypt
- ✅ Health check endpoints

## API Endpoints

### Authentication

```
POST /api/v1/auth/register - Register new user
POST /api/v1/auth/login - Login and get JWT token
GET /api/v1/auth/me - Get current user
POST /api/v1/auth/refresh - Refresh access token
```

### Users

```
GET /api/v1/users - List all users
GET /api/v1/users/{id} - Get user by ID
PUT /api/v1/users/{id} - Update user
DELETE /api/v1/users/{id} - Delete user
```

### Health

```
GET /health - Basic health check
GET /health/ready - Readiness check (includes dependencies)
GET /health/live - Liveness check
```

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run database migrations
alembic upgrade head

# Start service
uvicorn src.main:app --reload --port 8001

# Access API documentation
open http://localhost:8001/docs
```

## Testing

```bash
# Run tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src/ --cov-report=html

# View coverage report
open htmlcov/index.html
```

## Environment Variables

See `.env.example` in the root directory for required environment variables.

## Docker

```bash
# Build image
docker build -t openlearn/auth-service .

# Run container
docker run -p 8001:8001 --env-file .env openlearn/auth-service
```
