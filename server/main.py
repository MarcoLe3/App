from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.database import database
from search.client import ElasticsearchClient
from prometheus_fastapi_instrumentator import Instrumentator
from redis_fastapi import FastAPIRedis

from search import search_router
from booking import booking_router
from event import event_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    try:
        yield
    finally:
        await database.close()
        await ElasticsearchClient.es.close()

app = FastAPI(lifespan=lifespan)
FastAPIRedis(app).lifespan()

Instrumentator(
    excluded_handlers=["/metrics"],
).instrument(app).expose(
    app,
    endpoint="/metrics",
    include_in_schema=False,
)

app.include_router(search_router)
app.include_router(booking_router)
app.include_router(event_router)
