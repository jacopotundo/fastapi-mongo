from datetime import datetime
from typing import Optional

from beanie import PydanticObjectId
from bson import ObjectId
from pydantic import ConfigDict, Field, field_validator

from app.models.product.product_status_enum import ProductStatus
from app.schemas.product_schemas.product_base import ProductBase


class ProductResponse(ProductBase):
    """Schema di risposta"""

    id: PydanticObjectId = Field(alias="_id")
    created_at: datetime
    updated_at: Optional[datetime] = None
    status: ProductStatus

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )