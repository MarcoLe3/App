from fastapi import APIRouter, Depends, HTTPException, status
import asyncpg

from .service import get_events
from .schema import ListEventRequest
from core.database import database

router = APIRouter()

@router.get("/events")
async def get_list_of_events(request: ListEventRequest, pool: asyncpg.Pool = Depends(database.get_database_pool)) -> dict:
    try:
        events = await get_events(pool, request.limit, request.offset)
        if not events:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No events found")

        return {
            "status": "success",
            "events": events
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
