# Microservice Project - Testing & Automation Example

A complete full-stack microservice application for learning and testing automated building, testing, and deployment processes.

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
└── .github/workflows/         # CI/CD pipelines (optional)
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

## CI/CD Integration

### GitHub Actions Example Workflows

Create `.github/workflows/` directory and add:

- `backend-ci.yml` - Backend testing and building
- `frontend-ci.yml` - Frontend testing and building
- `deploy.yml` - Deployment pipeline

### Key Testing Commands

```bash
# Backend
pytest --cov --cov-report=xml  # For CI/CD coverage reports

# Frontend
npm test -- --coverage --watchAll=false  # For CI/CD
```

## Database Setup (Optional)

To add PostgreSQL support, update:

- `backend/requirements.txt` - Add `sqlalchemy`, `psycopg2-binary`
- `docker-compose.yml` - Add PostgreSQL service

## Environment Variables

### Backend (`.env`)

```
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### Frontend (`.env.local`)

```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Development Tools

### Backend

- **Framework**: FastAPI
- **Server**: Uvicorn
- **Testing**: Pytest
- **Validation**: Pydantic
- **ORM**: SQLAlchemy (optional)

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

## API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Common Tasks

### Clean Docker Resources

```bash
# Stop all containers
docker-compose down

# Remove images
docker-compose down --rmi all

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

## Troubleshooting

### Backend Connection Issues

```bash
# Check if backend is running
curl http://localhost:8000/health

# Check logs
docker-compose logs backend
```

### Frontend Connection Issues

```bash
# Verify API URL in .env.local
cat .env.local

# Check browser console for errors
```

### Port Already in Use

```bash
# Change ports in docker-compose.yml or use different ports:
docker run -p 8001:8000 fastapi-backend:latest
docker run -p 3001:3000 nextjs-frontend:latest
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

## Contributing

1. Follow the project structure
2. Write tests for new features
3. Update documentation
4. Use pre-commit hooks for linting

## Next Steps

1. **Add Database**: Implement PostgreSQL integration
2. **Add Auth**: Implement JWT authentication
3. **Add Caching**: Redis integration
4. **Add Monitoring**: Prometheus + Grafana
5. **Add Logging**: ELK stack or similar
6. **Deploy**: Deploy to DigitalOcean, AWS, or Azure

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Docker Documentation](https://docs.docker.com/)
- [Terraform Documentation](https://www.terraform.io/docs/)

## License

This project is open source and available for educational and testing purposes.
