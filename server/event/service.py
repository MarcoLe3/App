import asyncpg
from .sql_queries import GET_EVENTS

async def get_events(pool: asyncpg.Pool, limit: int, offset: int):
    async with pool.acquire() as connection:
        try:
            events = await connection.fetch(GET_EVENTS, limit, offset)
            return events
        except Exception as e:
            raise Exception(f"Error fetching events: {str(e)}")