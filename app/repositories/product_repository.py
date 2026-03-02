from typing import List, Optional

from app.models import Product


class ProductRepository:

    def __init__(self, db):
        self.db = db

    # paginazione per migliorare prestazioni con più prodotti
    # async def find_all_products(self, skip: int = 0, limit: int = 100) -> List[Product]:
    #     return await Product.find_all().skip(skip).limit(limit).to_list()

    async def find_all_products(self) -> List[Product]:
        return await Product.find_all().to_list()

    async def find_product_by_id(self, product_id: str) -> Optional[Product]:
        return await Product.get(product_id)

    async def create_product(self, product: Product) -> Product:
        await product.insert()
        return product

    async def update_product(self, product: Product) -> Product:
        await product.save()
        return product

    async def delete_product(self, product_id: str) -> bool:
        product = await Product.get(product_id)
        if product:
            await product.delete()
            return True
        return False