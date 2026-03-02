from typing import List

from fastapi import APIRouter, Depends, status

from app.dependencies import get_product_service
from app.schemas.product_schemas import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_service import ProductService


router = APIRouter()

@router.get("", response_model = List[ProductResponse], status_code = status.HTTP_200_OK)
async def get_all_products(product_service: ProductService = Depends(get_product_service)):
    return await product_service.get_all_products()

@router.get("/{product_id}", response_model = ProductResponse, status_code = status.HTTP_200_OK)
async def get_product_by_id(product_id: str, product_service: ProductService = Depends(get_product_service)):
    return await product_service.get_product_by_id(product_id)

@router.post("", response_model = ProductResponse, status_code = status.HTTP_201_CREATED)
async def create_product(product_to_create: ProductCreate, product_service: ProductService = Depends(get_product_service)):
    return await product_service.create_product(product_to_create)

@router.put("/{product_id}", response_model = ProductResponse, status_code = status.HTTP_200_OK)
async def update_product(product_id: str, product_to_update: ProductUpdate, product_service: ProductService = Depends(get_product_service)):
    return await product_service.update_product(product_id, product_to_update)

@router.delete("/{product_id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: str, product_service: ProductService = Depends(get_product_service)):
    return await product_service.delete_product(product_id)