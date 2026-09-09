from pydantic import BaseModel

class Event(BaseModel):
    id: int
    name: str
    description: str
    location: str
    date: str
    amount_of_tickets: int

class SearchRequest(BaseModel):
    query: str
    limit: int
    location: str | None = None
    date: str | None = None
    availability: str | None = None

class SearchResponse(BaseModel):
    result: list[Event]

class SearchFilter(BaseModel):
    location: str | None = None
    date: str | None = None
    availability: str | None = None