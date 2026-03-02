from pydantic import BaseModel, Field

from app.models.product.product_status_enum import ProductStatus


class ProductBase(BaseModel):
    """Campi base condivisi"""
    model_config = {"from_attributes": True}
    
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    quantity: int = Field(default=0, ge=0)