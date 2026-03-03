"""Product document model module.

This module defines the Product document model for MongoDB using Beanie ODM.
"""

from beanie import Document
from pydantic import Field
from datetime import datetime, timezone
from typing import Optional

from app.models.product.product_status_enum import ProductStatus


def utc_now() -> datetime:
    """Factory function for UTC datetime.
    
    Returns the current datetime in UTC timezone.
    Used as a default factory for timestamp fields.
    
    Returns:
        datetime: Current UTC datetime.
    """
    return datetime.now(timezone.utc)


class Product(Document):
    """Product document model for MongoDB.
    
    This class represents a product entity in the warehouse management system.
    It extends Beanie's Document class for ODM functionality.
    
    Attributes:
        name: Product name (required).
        price: Product price, must be greater than 0 (required).
        quantity: Product quantity in stock, defaults to 0, must be >= 0.
        status: Product status (STOCK or OUT_OF_STOCK), defaults to STOCK.
        created_at: UTC timestamp when the product was created.
        updated_at: Optional UTC timestamp of last update.
    
    Example:
        >>> product = Product(name="Widget", price=9.99, quantity=100)
        >>> await product.insert()
    """
    
    name: str = Field(...)  # required
    price: float = Field(..., gt=0)
    quantity: int = Field(default=0, ge=0)
    status: ProductStatus = Field(default=ProductStatus.STOCK)
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: Optional[datetime] = None

    class Settings:
        """Beanie document settings.
        
        Attributes:
            name: MongoDB collection name.
            use_state_management: Enable field tracking for updates.
        """
        name = "products"  # nome della collezione
        use_state_management = True  # attiva il tracking per capire quali campi sono da modificare
