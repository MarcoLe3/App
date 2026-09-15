from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from redis_fastapi import FastAPIRedis

from search import search_router
from booking import booking_router
from event import event_router
from core.lifespan import lifespan

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
