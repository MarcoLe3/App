from fastapi import APIRouter, Depends, HTTPException, status
from redis_fastapi import CacheBackendDep
from pydantic import BaseModel

router = APIRouter(tags=["bookings"])

class Payload(BaseModel):
    user_id: int

@router.post("/bookings/{event_id}/{ticket_id}")
async def create_booking(event_id: int, ticket_id: int, payload, cache: CacheBackendDep) -> dict:
    try:
        existing_ticket = await cache.get(f"{ticket_id}")

        if existing_ticket:
            return {
                "status": "failure"
            }
    except Exception as e:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))