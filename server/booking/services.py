import asyncpg
from fastapi import Depends

from core.database import database

async def create_booking(pool: asyncpg.Pool = Depends(database.get_connection)):
    pass