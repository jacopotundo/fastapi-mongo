from beanie import Document
from pydantic import Field
from datetime import datetime, timezone
from typing import Optional

from app.models.product.product_status_enum import ProductStatus


def utc_now() -> datetime: # non utilizzata da fastapi ma da pydantic
    """Factory function per datetime UTC"""
    return datetime.now(timezone.utc)

class Product(Document):
    name: str = Field(...) # ... sarebbe il required
    price: float = Field(..., gt=0)
    quantity: int = Field(default=0, ge=0)
    status: ProductStatus = Field(default=ProductStatus.STOCK)
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: Optional[datetime] = None

    class Settings:
        name = "products" # nome della collezione
        use_state_management = True # attiva il tracking per capire quali campi sono da modificare
