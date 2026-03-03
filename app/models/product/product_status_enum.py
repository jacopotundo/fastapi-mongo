"""Product status enumeration module.

This module defines the ProductStatus enum for representing
product stock status in the warehouse management system.
"""

from enum import Enum


class ProductStatus(str, Enum):
    """Product status enumeration for warehouse inventory.
    
    This enum defines the possible states of a product in the warehouse.
    It is equivalent to a Java enum in Spring Boot and is used in both
    database models and API schemas.
    
    Attributes:
        STOCK: Product is available in stock.
        OUT_OF_STOCK: Product is currently out of stock.
    
    Example:
        >>> status = ProductStatus.STOCK
        >>> print(status.value)
        stock
    """
    STOCK = "stock"
    OUT_OF_STOCK = "out_of_stock"