from typing import Optional

from pydantic import BaseModel, Field


class ProductUpdate(BaseModel):
    """Schema per update parziale"""
    model_config = {"from_attributes": True}
    
    name: Optional[str] = Field(None, min_length=1)
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)