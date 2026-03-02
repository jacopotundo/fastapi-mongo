from beanie import init_beanie

from app.core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.product.product import Product   

class Database:
    # creo il client a livello di classe non di istanza
    __client: AsyncIOMotorClient | None = None
    __database = None
    
    @classmethod
    async def connect(cls):
        #controllo se non è presente già una connessione altrimenti la creo
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
        #controllo se è presente la connessione e la chiudo
        if cls.__client:
            cls.__client.close()
            cls.__client = None
            cls.__database = None

    @classmethod
    def get_database(cls):
        if cls.__database is None:
            raise RuntimeError("Database non inizializzato. Chiama connect() prima.")
        return cls.__database
