"""Product create schema module.

This module defines the schema for product creation requests.
"""

from app.schemas.product_schemas.product_base import ProductBase


class ProductCreate(ProductBase):
    """Schema for product creation requests.
    
    This class extends ProductBase and is used to validate incoming
    data when creating a new product. All fields are required
    (except quantity which has a default).
    
    Example:
        >>> product_data = ProductCreate(name="Widget", price=9.99, quantity=100)
    """
    pass