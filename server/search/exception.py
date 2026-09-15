from fastapi.responses import JSONResponse
from fastapi import APIRouter, Request, status
from datetime import datetime
import uuid

router = APIRouter()

class SearchNotFoundException(Exception):
    def __init__(self, query: str):
        self.query = query

@router.exception_handler(SearchNotFoundException)
async def search_not_found_exception_handler(request: Request, exc: SearchNotFoundException):
    return JSONResponse (
        status = "error",
        status_code = status.HTTP_404_NOT_FOUND,
        error = {
            "code": "RESOURCE_NOT_FOUND",
            "message": "search is not found",
            "details": f"{exc.query} was not found",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "suggestion": "check elastic search"
        },
        requestId = str(uuid.uuid4())
    )