from fastapi import APIRouter, status
from app.core.config import settings


health_router = APIRouter()

@health_router.get("", status_code = status.HTTP_200_OK)
async def health_check():
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "statusCode": 200
        }