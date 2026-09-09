from pydantic import BaseModel

class Ticket(BaseModel):
    id: int
    event_id: int
    seat_row: str
    seat_number: int
    status: str
    amount: int = 1

class BookingRequest(BaseModel):
    user_id: int
    event_id: int
    ticket_id: int

class BookingResponse(BaseModel):
    status: str
    message: str