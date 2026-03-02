from typing import List, Optional

from fastapi import HTTPException, status
from datetime import datetime, time, timezone


from app.repositories.product_repository import ProductRepository
from app.schemas import ProductResponse, ProductCreate, ProductUpdate
from app.models.product import Product, ProductStatus

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def get_all_products(self) -> List[ProductResponse]:
        products_list = await self.repository.find_all_products()
        return [ProductResponse.model_validate(product) for product in products_list]
    
    async def get_product_by_id(self, product_id: str) -> Optional[ProductResponse]:
        product = await self.repository.find_product_by_id(product_id)
        if product is None:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Product with id {product_id} not found")
        return ProductResponse.model_validate(product)

    async def create_product(self, product_to_create: ProductCreate) -> ProductResponse:
        # status = ProductStatus.OUT_OF_STOCK if data.quantity == 0 else ProductStatus.STOCK
        product_to_save = Product (
            name = product_to_create.name,
            price = product_to_create.price,
            quantity = product_to_create.quantity,
            status = status_checker(product_to_create.quantity),
            created_at = datetime.now(timezone.utc)
            )
        
        product_saved = await self.repository.create_product(product_to_save)
        return ProductResponse.model_validate(product_saved)

    async def update_product(self, product_id: str,  product_to_update: ProductUpdate) -> ProductResponse:
        existing_product = await self.repository.find_product_by_id(product_id)
        
        if existing_product is None:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Product with id {product_id} not found")

        update_data = product_to_update.model_dump(exclude_unset = True)
        for field, value in update_data.items():
            setattr(existing_product, field, value)

        new_quantity = product_to_update.quantity if product_to_update.quantity is not None else existing_product.quantity
        existing_product.status = status_checker(new_quantity)
        
        existing_product.updated_at = datetime.now(timezone.utc)
        
        product_updated = await self.repository.update_product(existing_product)
        return ProductResponse.model_validate(product_updated)

    async def delete_product(self, product_id: str) -> bool:
        return await self.repository.delete_product(product_id)

def status_checker(product_quantity: int) -> ProductStatus:
    if product_quantity > 0:
        status = ProductStatus.STOCK
    else:
        status = ProductStatus.OUT_OF_STOCK
    return status