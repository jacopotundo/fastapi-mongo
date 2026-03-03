"""Application configuration module.

This module provides settings management using pydantic-settings,
loading configuration from environment variables.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables.
    
    This class manages all configuration parameters for the application,
    including MongoDB connection, application metadata, and API settings.
    
    Attributes:
        MONGODB_URL: MongoDB connection string.
        DATABASE_NAME: Name of the MongoDB database.
        APP_NAME: Application display name. Defaults to "Warehouse API".
        API_V1_STR: API version 1 prefix string. Defaults to "/api/v1".
        DEBUG: Debug mode flag. Defaults to True.
    
    Example:
        >>> settings = Settings()
        >>> print(settings.APP_NAME)
        Warehouse API
    """
    
    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding  = "utf-8",
        case_sensitive = False,
        extra = "ignore"
    )

    # MongoDB
    MONGODB_URL: str
    DATABASE_NAME: str

    # Application
    APP_NAME: str = "Warehouse API"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = True

    # JWT (placeholder per dopo)
    # JWT_SECRET_KEY: str = "change-me-in-production"
    # JWT_ALGORITHM: str = "HS256"

    @property
    def database_url(self) -> str:
        """Get the MongoDB database URL.
        
        Returns:
            str: The MongoDB connection URL.
        """
        return self.MONGODB_URL


# Istanza del singleton di settings
settings = Settings()