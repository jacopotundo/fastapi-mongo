"""Product response schema module.

This module defines the schema for product API responses.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from beanie import PydanticObjectId
from pydantic import ConfigDict, Field

from app.models.product.product_status_enum import ProductStatus
from app.schemas.product_schemas.product_base import ProductBase


class ProductResponse(ProductBase):
    """Schema for product API responses.

    This class extends ProductBase and includes additional fields
    returned by the API, such as the product ID, timestamps, and status.

    Attributes:
        id: MongoDB ObjectId of the product.
        name: Product name.
        price: Product price.
        quantity: Product quantity in stock.
        created_at: UTC timestamp when the product was created.
        updated_at: Optional UTC timestamp of last update.
        status: Product status (STOCK or OUT_OF_STOCK).

    Example:
        >>> response = ProductResponse(
        ...     id="507f1f77bcf86cd799439011",
        ...     name="Widget",
        ...     price=9.99,
        ...     quantity=100,
        ...     created_at=datetime.now(),
        ...     status=ProductStatus.STOCK
        ... )
    """

    id: PydanticObjectId = Field(alias="_id")
    created_at: datetime
    updated_at: Optional[datetime] = None
    status: ProductStatus

    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True
    )