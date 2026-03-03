"""Health check router module.

This module provides health check endpoints for monitoring
the application status.
"""

from fastapi import APIRouter, status
from app.core.config import settings


health_router = APIRouter()


@health_router.get("", status_code=status.HTTP_200_OK)
async def health_check():
    """Perform a health check on the service.
    
    This endpoint returns the current health status of the application,
    including the service name and status code. It can be used by
    load balancers, orchestrators, or monitoring systems to verify
    that the service is running.
    
    Returns:
        dict: A dictionary containing:
            - status (str): Health status ("healthy").
            - service (str): Application name from settings.
            - statusCode (int): HTTP status code (200).
    
    Example:
        >>> # GET /health
        >>> # Response: {"status": "healthy", "service": "Warehouse API", "statusCode": 200}
    """
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "statusCode": 200
    }