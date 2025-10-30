"""
FastAPI Application Entry Point with PostgreSQL Integration
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import health, users, products
from app.database import init_db

# Initialize database tables on startup (skip during tests)
if os.getenv("TESTING") != "true":
    init_db()

app = FastAPI(
    title="Microservice API",
    description="FastAPI backend with PostgreSQL database",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router, tags=["Health"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(products.router, prefix="/api/v1/products", tags=["Products"])

@app.get("/")
def read_root():
    """Root endpoint"""
    return {
        "message": "Welcome to Microservice API",
        "version": "1.0.0",
        "docs": "/docs",
        "database": "PostgreSQL"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
