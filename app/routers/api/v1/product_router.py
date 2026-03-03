"""Product API router module.

This module defines the REST API endpoints for product management,
including CRUD operations for products.
"""

from typing import List

from fastapi import APIRouter, Depends, status

from app.dependencies import get_product_service
from app.schemas.product_schemas import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_service import ProductService


router = APIRouter()


@router.get("", response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
async def get_all_products(product_service: ProductService = Depends(get_product_service)):
    """Retrieve all products from the warehouse.
    
    This endpoint returns a list of all products stored in the database.
    
    Args:
        product_service: ProductService instance injected via dependency injection.
        
    Returns:
        List[ProductResponse]: List of all products.
    """
    return await product_service.get_all_products()


@router.get("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product_by_id(product_id: str, product_service: ProductService = Depends(get_product_service)):
    """Retrieve a specific product by its ID.
    
    This endpoint returns a single product identified by its MongoDB ObjectId.
    
    Args:
        product_id: The MongoDB ObjectId of the product as a string.
        product_service: ProductService instance injected via dependency injection.
        
    Returns:
        ProductResponse: The requested product.
        
    Raises:
        HTTPException: 404 if product not found.
    """
    return await product_service.get_product_by_id(product_id)


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product_to_create: ProductCreate, product_service: ProductService = Depends(get_product_service)):
    """Create a new product in the warehouse.
    
    This endpoint creates a new product with the provided data.
    
    Args:
        product_to_create: Product data for creation (name, price, quantity).
        product_service: ProductService instance injected via dependency injection.
        
    Returns:
        ProductResponse: The created product with generated fields.
    """
    return await product_service.create_product(product_to_create)


@router.put("/{product_id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def update_product(product_id: str, product_to_update: ProductUpdate, product_service: ProductService = Depends(get_product_service)):
    """Update an existing product.
    
    This endpoint updates a product identified by its ID with the provided data.
    Only provided fields will be updated (partial update supported).
    
    Args:
        product_id: The MongoDB ObjectId of the product as a string.
        product_to_update: Product data to update (partial).
        product_service: ProductService instance injected via dependency injection.
        
    Returns:
        ProductResponse: The updated product.
        
    Raises:
        HTTPException: 404 if product not found.
    """
    return await product_service.update_product(product_id, product_to_update)


@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str, product_service: ProductService = Depends(get_product_service)):
    """Delete a product by its ID.
    
    This endpoint deletes a product identified by its MongoDB ObjectId.
    
    Args:
        product_id: The MongoDB ObjectId of the product as a string.
        product_service: ProductService instance injected via dependency injection.
        
    Returns:
        None: Returns 204 No Content on success.
    """
    return await product_service.delete_product(product_id)