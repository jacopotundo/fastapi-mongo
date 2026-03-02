from fastapi import Depends

from app.core.database import Database
from app.repositories.product_repository import ProductRepository
from app.services.product_service import ProductService


async def get_database():
    return Database.get_database()

async def get_product_repository(db = Depends(get_database)) -> ProductRepository:
    return ProductRepository(db=db)

async def get_product_service(repository = Depends(get_product_repository)) -> ProductService:
    return ProductService(repository = repository)
