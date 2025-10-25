"""Health check endpoints"""
from fastapi import APIRouter, status

router = APIRouter()

@router.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """
    Health check endpoint
    Returns the status of the API
    """
    return {
        "status": "healthy",
        "service": "microservice-api",
        "version": "1.0.0"
    }

@router.get("/readiness", status_code=status.HTTP_200_OK)
def readiness_check():
    """
    Readiness check endpoint
    Returns the readiness status of the API
    """
    return {
        "ready": True,
        "message": "API is ready to receive requests"
    }
