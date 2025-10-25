# Backend - FastAPI Microservice

## Overview

This is a FastAPI-based backend microservice for testing automated building, testing, and deployment processes.

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   ├── health.py      # Health check endpoints
│   │   ├── users.py       # User management endpoints
│   │   └── products.py    # Product management endpoints
│   ├── models/            # Database models
│   └── schemas/           # Pydantic schemas
├── tests/
│   ├── test_health.py     # Health check tests
│   ├── test_users.py      # User endpoint tests
│   └── test_products.py   # Product endpoint tests
├── main.py                # Application entry point
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── .dockerignore           # Docker ignore file
├── pytest.ini             # Pytest configuration
└── .env.example           # Environment variables template
```

## Installation

### Prerequisites

- Python 3.11+
- pip or poetry
- Docker (optional)

### Setup

1. Create virtual environment:

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python main.py
   ```

   Or with uvicorn:

   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Health Check

- `GET /health` - Health status
- `GET /readiness` - Readiness status

### Users

- `GET /api/v1/users/` - List all users
- `GET /api/v1/users/{id}` - Get specific user
- `POST /api/v1/users/` - Create user
- `PUT /api/v1/users/{id}` - Update user
- `DELETE /api/v1/users/{id}` - Delete user

### Products

- `GET /api/v1/products/` - List all products
- `GET /api/v1/products/{id}` - Get specific product
- `POST /api/v1/products/` - Create product
- `PUT /api/v1/products/{id}` - Update product
- `DELETE /api/v1/products/{id}` - Delete product

## Testing

### Run all tests

```bash
pytest
```

### Run tests with coverage

```bash
pytest --cov=app --cov-report=html
```

### Run specific test file

```bash
pytest tests/test_health.py -v
```

## Docker

### Build image

```bash
docker build -t fastapi-backend:latest .
```

### Run container

```bash
docker run -p 8000:8000 fastapi-backend:latest
```

## API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Environment Variables

Create a `.env` file based on `.env.example`:

```
APP_NAME=Microservice API
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Development

### Code Style

Uses FastAPI best practices and PEP 8

### Hot Reload

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## CI/CD Integration

This project is ready for CI/CD pipelines:

- GitHub Actions
- GitLab CI
- Jenkins
- Azure DevOps

See `.github/workflows` for GitHub Actions examples.
