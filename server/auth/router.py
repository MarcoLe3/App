from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Response
from pydantic import BaseModel

from datetime import timedelta
from .service import authentication_user
from core.config import settings

router = APIRouter()

class LoginRequest(BaseModel):
    username: str
    password: str

@router.get("/auth/token")
async def login_for_access_token(user_header: LoginRequest, response: Response) -> Token:
    user = authentication_user(username, password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expire = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id}, expires_delta=access_token_expire
    )

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=True
    )