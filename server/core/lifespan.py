from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.database import database
from search.client import ElasticsearchClient

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    try:
        yield
    finally:
        await database.close()
        await ElasticsearchClient.es.close()