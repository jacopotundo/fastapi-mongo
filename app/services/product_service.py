"""Product service module.

This module provides business logic for product management,
orchestrating between controllers and repositories.
"""

from typing import List, Optional

from fastapi import HTTPException, status
from datetime import datetime, timezone


from app.repositories.product_repository import ProductRepository
from app.schemas.product_schemas import ProductResponse, ProductCreate, ProductUpdate
from app.models.product.product import Product, ProductStatus


class ProductService:
    """Service for product business logic.
    
    This class implements the service layer pattern, providing methods
    for product CRUD operations with business logic validation.
    It uses ProductRepository for data access.
    
    Attributes:
        repository: ProductRepository instance for data access.
    
    Example:
        >>> service = ProductService(repository)
        >>> products = await service.get_all_products()
    """
    
    def __init__(self, repository: ProductRepository):
        """Initialize the ProductService.
        
        Args:
            repository: ProductRepository instance for data access.
        """
        self.repository = repository

    async def get_all_products(self) -> List[ProductResponse]:
        """Retrieve all products from the warehouse.
        
        Returns:
            List[ProductResponse]: List of all products.
        """
        products_list = await self.repository.find_all_products()
        return [ProductResponse.model_validate(product) for product in products_list]

    async def get_product_by_id(self, product_id: str) -> Optional[ProductResponse]:
        """Retrieve a specific product by its ID.
        
        Args:
            product_id: The MongoDB ObjectId of the product as a string.
            
        Returns:
            Optional[ProductResponse]: The requested product.
            
        Raises:
            HTTPException: 404 if product not found.
        """
        product = await self.repository.find_product_by_id(product_id)
        if product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")
        return ProductResponse.model_validate(product)

    async def create_product(self, product_to_create: ProductCreate) -> ProductResponse:
        """Create a new product in the warehouse.
        
        Args:
            product_to_create: Product data for creation.
            
        Returns:
            ProductResponse: The created product with generated fields.
        """
        product_to_save = Product(
            name=product_to_create.name,
            price=product_to_create.price,
            quantity=product_to_create.quantity,
            status=status_checker(product_to_create.quantity),
            created_at=datetime.now(timezone.utc)
        )

        product_saved = await self.repository.create_product(product_to_save)
        return ProductResponse.model_validate(product_saved)

    async def update_product(self, product_id: str, product_to_update: ProductUpdate) -> ProductResponse:
        """Update an existing product.
        
        Args:
            product_id: The MongoDB ObjectId of the product as a string.
            product_to_update: Product data to update (partial).
            
        Returns:
            ProductResponse: The updated product.
            
        Raises:
            HTTPException: 404 if product not found.
        """
        existing_product = await self.repository.find_product_by_id(product_id)

        if existing_product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with id {product_id} not found")

        update_data = product_to_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(existing_product, field, value)

        new_quantity = product_to_update.quantity if product_to_update.quantity is not None else existing_product.quantity
        existing_product.status = status_checker(new_quantity)

        existing_product.updated_at = datetime.now(timezone.utc)

        product_updated = await self.repository.update_product(existing_product)
        return ProductResponse.model_validate(product_updated)

    async def delete_product(self, product_id: str) -> bool:
        """Delete a product by its ID.
        
        Args:
            product_id: The MongoDB ObjectId of the product as a string.
            
        Returns:
            bool: True if product was deleted, False if not found.
        """
        return await self.repository.delete_product(product_id)


def status_checker(product_quantity: int) -> ProductStatus:
    """Determine product status based on quantity.
    
    Args:
        product_quantity: The quantity of the product in stock.
        
    Returns:
        ProductStatus: STOCK if quantity > 0, OUT_OF_STOCK otherwise.
    """
    if product_quantity > 0:
        status = ProductStatus.STOCK
    else:
        status = ProductStatus.OUT_OF_STOCK
    return status