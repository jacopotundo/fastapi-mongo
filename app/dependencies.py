"""FastAPI dependency injection module.

This module provides reusable dependency injection functions for FastAPI,
enabling clean separation of concerns and easier testing.
"""

from fastapi import Depends

from app.core.database import Database
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService


async def get_database():
    """Get the database instance.
    
    This dependency provides the database instance to routes and services.
    It uses the Database singleton to retrieve the active connection.
    
    Returns:
        The MongoDB database instance.
        
    Raises:
        RuntimeError: If database connection is not initialized.
    """
    return Database.get_database()


async def get_product_repository(db=Depends(get_database)) -> ProductRepository:
    """Get a ProductRepository instance.
    
    This dependency injects a ProductRepository with the database connection,
    enabling repository pattern usage in services.
    
    Args:
        db: Database instance injected via get_database dependency.
        
    Returns:
        ProductRepository: Repository instance for product operations.
    """
    return ProductRepository(db=db)


async def get_product_service(repository=Depends(get_product_repository)) -> ProductService:
    """Get a ProductService instance.
    
    This dependency injects a ProductService with a ProductRepository,
    enabling service layer usage in route handlers.
    
    Args:
        repository: ProductRepository instance injected via get_product_repository.
        
    Returns:
        ProductService: Service instance for product business logic.
    """
    return ProductService(repository=repository)
