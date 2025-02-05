import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MASTER_DB_URL: str = os.getenv("MASTER_DB_URL", "localhost")
    DB_HOST: str = os.getenv("DB_HOST", "db")
    DB_USER: str = os.getenv("DB_USER", "admin")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "adminpass")
    
    class Config:
        env_file = ".env"
        
settings = Settings()
