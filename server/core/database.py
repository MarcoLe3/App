import asyncpg
from .config import settings

class Database:
    def __init__(self):
        self.database_pool = None

    async def connect(self):
        self.database_pool = await asyncpg.create_pool(
            dsn=settings.DATABASE_URL,
            min_size=settings.DB_MIN_SIZE_POOL,
            max_size=settings.DB_MAX_SIZE_POOL,
        )

    async def close(self):
        if self.database_pool:
            await self.database_pool.close()
    
    def get_database_pool(self):
        if not self.database_pool:
            raise Exception("Database pool is not initialized.")

        return self.database_pool
    

database = Database()