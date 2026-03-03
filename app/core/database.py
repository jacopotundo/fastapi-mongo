"""Database connection and management module.

This module provides a singleton database connection manager for MongoDB
using Motor (async MongoDB driver) and Beanie ODM.
"""

from beanie import init_beanie

from app.core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.product.product import Product


class Database:
    """Database connection manager using singleton pattern.
    
    This class manages MongoDB connections using class-level methods,
    ensuring a single connection instance across the application.
    It initializes Beanie ODM for document mapping.
    
    Attributes:
        __client: Motor async client instance (class-level).
        __database: Database instance reference (class-level).
    
    Example:
        >>> await Database.connect()
        >>> db = Database.get_database()
        >>> await Database.close()
    """
    
    # creo il client a livello di classe non di istanza
    __client: AsyncIOMotorClient | None = None
    __database = None

    @classmethod
    async def connect(cls):
        """Establish connection to MongoDB database.
        
        Creates a new Motor client connection if not already established,
        initializes Beanie with document models, and sets up the database
        reference.
        
        Raises:
            Exception: If MongoDB connection fails.
        """
        # controllo se non è presente già una connessione altrimenti la creo
        if cls.__client is None:
            cls.__client = AsyncIOMotorClient(settings.MONGODB_URL)
            cls.__database = cls.__client[settings.DATABASE_NAME]

            # inizializzazione beanie con i modelli
            await init_beanie(
                database = cls.__database,
                document_models = [Product]
            )

    @classmethod
    async def close(cls):
        """Close the MongoDB connection.
        
        Closes the active client connection and resets both client
        and database references to None.
        """
        # controllo se è presente la connessione e la chiudo
        if cls.__client:
            cls.__client.close()
            cls.__client = None
            cls.__database = None

    @classmethod
    def get_database(cls):
        """Get the current database instance.
        
        Returns:
            The database instance if connected.
            
        Raises:
            RuntimeError: If database connection has not been initialized.
                Call connect() before calling this method.
        """
        if cls.__database is None:
            raise RuntimeError("Database non inizializzato. Chiama connect() prima.")
        return cls.__database
