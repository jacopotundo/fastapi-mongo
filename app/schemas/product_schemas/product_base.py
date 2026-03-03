"""Product base schema module.

This module defines the base schema for product data validation
using Pydantic.
"""

from pydantic import BaseModel, Field

from app.models.product.product_status_enum import ProductStatus


class ProductBase(BaseModel):
    """Base schema for product data.
    
    This class defines the common fields shared across all product-related
    schemas (create, update, response). It provides validation rules
    for product attributes.
    
    Attributes:
        name: Product name, must be at least 1 character.
        price: Product price, must be greater than 0.
        quantity: Product quantity in stock, defaults to 0, must be >= 0.
    
    Example:
        >>> product = ProductBase(name="Widget", price=9.99, quantity=100)
    """
    
    model_config = {"from_attributes": True}

    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    quantity: int = Field(default=0, ge=0)