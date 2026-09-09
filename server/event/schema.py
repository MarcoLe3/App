from pydantic import BaseModel

class Event(BaseModel):
    id: int
    name: str
    description: str
    location: str
    date: str
    amount_of_tickets: int

class EventResponse(BaseModel):
    events: list[Event]

class ListEventRequest(BaseModel):
    limit: int = 20
    offset: int = 0