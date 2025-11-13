# Microservice Project - Testing & Automation 

A complete full-stack microservice application for learning and testing automated building, testing, and deployment processes.

## Architecture

![DevOps Architecture Diagram](./imgs/architecture.gif)


## Project Structure

```
DevOps/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── api/               # API endpoints
│   │   ├── models/            # Database models
│   │   └── schemas/           # Pydantic schemas
│   ├── tests/                 # Unit & integration tests
│   ├── main.py                # Application entry point
│   ├── requirements.txt        # Python dependencies
│   ├── Dockerfile             # Docker configuration
│   └── pytest.ini             # Pytest configuration
│
├── frontend/                   # Next.js Frontend
│   ├── src/
│   │   ├── pages/             # Next.js pages
│   │   ├── components/        # React components
│   │   ├── services/          # API client
│   │   └── types/             # TypeScript types
│   ├── __tests__/             # Unit tests
│   ├── package.json           # Node dependencies
│   ├── tsconfig.json          # TypeScript config
│   ├── jest.config.ts         # Jest testing
│   ├── Dockerfile             # Docker configuration
│   └── next.config.js         # Next.js config
│
├── docker-compose.yml         # Multi-container orchestration
├── terraform/                 # Infrastructure as Code

```


## Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Start both services
docker-compose up -d

# Access services
Frontend: http://localhost:3000
Backend API: http://localhost:8000
Swagger Docs: http://localhost:8000/docs
```

### Option 2: Run Locally

#### Backend (FastAPI)

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
# Or with hot reload
uvicorn main:app --reload
```

Backend will be available at http://localhost:8000

#### Frontend (Next.js)

```bash
cd frontend

# Install dependencies
npm install

# Create environment file
echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local

# Run development server
npm run dev
```

Frontend will be available at http://localhost:3000

## Features

### Backend (FastAPI)

- ✅ **RESTful API** - User and Product management endpoints
- ✅ **Health Checks** - Health and readiness probes
- ✅ **CORS Support** - Cross-origin requests handling
- ✅ **Type Safety** - Pydantic models for validation
- ✅ **Comprehensive Testing** - Unit and integration tests with pytest
- ✅ **Docker Support** - Production-ready Dockerfile
- ✅ **API Documentation** - Auto-generated Swagger UI and ReDoc

### Frontend (Next.js)

- ✅ **Server-Side Rendering** - Optimized for performance
- ✅ **TypeScript** - Full type safety
- ✅ **Tailwind CSS** - Utility-first styling
- ✅ **Component Architecture** - Reusable React components
- ✅ **API Integration** - Axios client for backend communication
- ✅ **Testing** - Jest and React Testing Library
- ✅ **Docker Support** - Multi-stage build optimization

## API Endpoints

### Health Check

```
GET /health          # Health status
GET /readiness       # Readiness probe
```

### Users

```
GET /api/v1/users/           # List all users
GET /api/v1/users/{id}       # Get specific user
POST /api/v1/users/          # Create user
PUT /api/v1/users/{id}       # Update user
DELETE /api/v1/users/{id}    # Delete user
```

### Products

```
GET /api/v1/products/        # List all products
GET /api/v1/products/{id}    # Get specific product
POST /api/v1/products/       # Create product
PUT /api/v1/products/{id}    # Update product
DELETE /api/v1/products/{id} # Delete product
```

## Testing

### Backend Tests

```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_health.py -v
```

### Frontend Tests

```bash
cd frontend

# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run in watch mode
npm run test:watch
```

## Building Docker Images

### Build Individual Images

```bash
# Backend
cd backend
docker build -t fastapi-backend:latest .

# Frontend
cd frontend
docker build -t nextjs-frontend:latest .
```

### Run Individual Containers

```bash
# Backend
docker run -p 8000:8000 fastapi-backend:latest

# Frontend
docker run -p 3000:3000 -e NEXT_PUBLIC_API_URL=http://localhost:8000 nextjs-frontend:latest
```

### Key Testing Commands

```bash
# Backend
pytest --cov --cov-report=xml  # For CI/CD coverage reports

# Frontend
npm test -- --coverage --watchAll=false  # For CI/CD
```

## Database Setup (Optional)

To add PostgreSQL support, update:

- `backend/requirements.txt`
- `docker-compose.yml` - Add PostgreSQL service

## Security & Firewall Configuration

This project is deployed on DigitalOcean with a secure firewall configuration to restrict backend access.

### Firewall Rules

- **Backend API (Port 8000)**: Access restricted to:

  - Frontend VM droplet (internal DigitalOcean network)
  - My personal machine (via my public IP)
  - Backend localhost (for internal testing)

- **Frontend (Port 3000)**: Open to all (public facing)
- **SSH Access**: Restricted to my personal machine's public IP only

### Trusted IP Management

My public IP is configured in `terraform/digitalocean/secret.auto.tfvars`:

```
# This file is NOT committed to git (.gitignore protected)
trusted_ip = "YOUR.PUBLIC.IP/32"
```

**To update your IP:**

1. Discover your current public IP:

   ```bash
   # Windows
   Invoke-RestMethod https://ipinfo.io/ip

   # Linux/Mac
   curl https://ipinfo.io/ip
   ```

2. Update `terraform/digitalocean/secret.auto.tfvars`:

   ```
   trusted_ip = "NEW.IP.ADDRESS/32"
   ```

3. Apply firewall changes:
   ```bash
   cd terraform/digitalocean
   terraform apply -var-file=secret.auto.tfvars
   ```

### CORS Configuration

Backend CORS is configured via environment variables during Jenkins deployment. The `CORS_ORIGINS` includes:

- Frontend VM
- Backend VM (for internal communication)
- Localhost (for development)

This allows the frontend to safely communicate with the backend API.

## Environment Variables

### Backend (`.env`)

```
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost/dbname
```

## Development Tools

### Backend

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Testing**: Pytest
- **Validation**: Pydantic
- **ORM**: SQLAlchemy

### Frontend

- **Framework**: Next.js 14
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Testing**: Jest & React Testing Library
- **HTTP Client**: Axios

## Documentation

- **Backend**: [Backend README](./backend/README.md)
- **Frontend**: [Frontend README](./frontend/README.md)
- **Terraform**: [Terraform README](./terraform/README.md)
- **Ansible**: [Ansible README](./ansible/README.md)
- **JENKINS**: [Jenkins README](./jenkins/README.md)

## API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Common Tasks

### Clean Docker Resources

```bash
# Stop all containers
docker-compose down

# Remove volumes
docker-compose down -v
```

### View Logs

```bash
# Backend logs
docker-compose logs -f backend

# Frontend logs
docker-compose logs -f frontend

# Both
docker-compose logs -f
```

### Rebuild Services

```bash
# Rebuild without cache
docker-compose up -d --build --no-cache

# Rebuild specific service
docker-compose up -d --build backend
```

## Performance Optimization

### Backend

- Connection pooling for databases
- Caching strategies
- Async/await for I/O operations

### Frontend

- Code splitting with Next.js
- Image optimization
- CSS purging with Tailwind

## Security Considerations

- Environment variables for sensitive data
- CORS configuration
- Input validation with Pydantic
- SQL injection prevention with SQLAlchemy ORM
- XSS prevention with React
