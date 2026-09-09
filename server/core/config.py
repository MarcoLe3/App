from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Setting(BaseSettings):
    #Auth
    SECRET_KEY: str = "22cda67d26b53198335fcca6297016c8235a1cd39d51576e64a46d495a0f1fb2"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/mydatabase")
    DB_MIN_SIZE_POOL: int = 5
    DB_MAX_SIZE_POOL: int = 20

    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")

    # Elasticsearch
    ELASTICSEARCH_URL: str = os.getenv("ELASTICSEARCH_URL")
    

settings = Setting()
