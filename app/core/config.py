from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding  = "utf-8",
        case_sensitive = False,
        extra = "ignore"
    )
    
    # MongoDB
    MONGODB_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "warehouse_dev"
    
    # Application
    APP_NAME: str = "Warehouse API"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True
    
    # JWT (placeholder per dopo)
    JWT_SECRET_KEY: str = "change-me-in-production"
    JWT_ALGORITHM: str = "HS256"
    
    @property
    def database_url(self) -> str:
        # Metodo helper per accesso al db
        return self.MONGODB_URL # posso usarla come attributo e non come metodo
    
# Istanza del singleton di settings
settings = Settings()