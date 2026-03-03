"""Product repository module.

This module provides data access layer for Product entities,
implementing CRUD operations using Beanie ODM.
"""

from typing import List, Optional

from app.models.product.product import Product


class ProductRepository:
    """Repository for Product CRUD operations.
    
    This class provides methods to interact with the products collection
    in MongoDB using Beanie ODM. It implements the repository pattern
    for clean separation of data access logic.
    
    Attributes:
        db: Database instance for product operations.
    
    Example:
        >>> repo = ProductRepository(db)
        >>> products = await repo.find_all_products()
    """

    def __init__(self, db):
        """Initialize the ProductRepository.
        
        Args:
            db: Database instance for product operations.
        """
        self.db = db

    async def find_all_products(self) -> List[Product]:
        """Retrieve all products from the database.
        
        Returns:
            List[Product]: List of all product documents.
        """
        return await Product.find_all().to_list()
    
    # paginazione per migliorare prestazioni con più prodotti
    # async def find_all_products(self, skip: int = 0, limit: int = 100) -> List[Product]:
    #     return await Product.find_all().skip(skip).limit(limit).to_list()


    async def find_product_by_id(self, product_id: str) -> Optional[Product]:
        """Find a product by its ID.
        
        Args:
            product_id: The MongoDB ObjectId of the product as a string.
            
        Returns:
            Optional[Product]: The product if found, None otherwise.
        """
        return await Product.get(product_id)

    async def create_product(self, product: Product) -> Product:
        """Create a new product in the database.
        
        Args:
            product: Product instance to be created.
            
        Returns:
            Product: The created product with generated fields.
        """
        await product.insert()
        return product

    async def update_product(self, product: Product) -> Product:
        """Update an existing product in the database.
        
        Args:
            product: Product instance with updated fields.
            
        Returns:
            Product: The updated product.
        """
        await product.save()
        return product

    async def delete_product(self, product_id: str) -> bool:
        """Delete a product by its ID.
        
        Args:
            product_id: The MongoDB ObjectId of the product as a string.
            
        Returns:
            bool: True if product was deleted, False if not found.
        """
        product = await Product.get(product_id)
        if product:
            await product.delete()
            return True
        return False