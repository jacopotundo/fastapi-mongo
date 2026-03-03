"""FastAPI application main module.

This module initializes and configures the FastAPI application,
including lifespan events, routers, and middleware.
"""

from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.config import settings
from app.core.database import Database
from app.routers import health_router
from app.routers.api.v1 import router

from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup and shutdown events.
    
    This context manager handles database connection lifecycle:
    - Connects to MongoDB on application startup
    - Closes connection on application shutdown
    
    Args:
        app: FastAPI application instance.
        
    Yields:
        None: Control returns to FastAPI to handle requests.
    """
    await Database.connect()  # Connette ALL'AVVIO
    yield
    await Database.close()  # Chiude ALLO SHUTDOWN


app = FastAPI(
    title=settings.APP_NAME,
    lifespan=lifespan
)

app.include_router(
    router,
    prefix=f"{settings.API_V1_STR}/products",
    tags=["Products"]
)

app.include_router(
    health_router,
    prefix="/health",
    tags=["Health Check"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O metti l'URL specifico del tuo frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)