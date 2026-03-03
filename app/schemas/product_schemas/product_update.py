"""Product update schema module.

This module defines the schema for product update requests.
"""

from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ProductUpdate(BaseModel):
    """Schema for partial product update requests.

    This class is used to validate incoming data when updating an existing
    product. All fields are optional to support partial updates.

    Attributes:
        name: Optional product name, must be at least 1 character if provided.
        price: Optional product price, must be greater than 0 if provided.
        quantity: Optional product quantity, must be >= 0 if provided.

    Example:
        >>> update_data = ProductUpdate(quantity=50)  # Only update quantity
    """

    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = Field(None, min_length=1)
    price: Optional[float] = Field(None, gt=0)
    quantity: Optional[int] = Field(None, ge=0)