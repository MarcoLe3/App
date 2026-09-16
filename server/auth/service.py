import jwt
from fastapi import APIRouter, Depends, HTTPException, Header, status
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from typing import Annotated
from pydantic import BaseModel

from core import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

router = APIRouter()
password_hash = PasswordHash()

class Token(BaseModel):
    access_token: str
    token_type: str

def get_user(db, username: str):
    if user := db.get(username):
        return user

def create_access_token(data: dict, expires_delta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def vertify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

def get_hash_password(plain_password: str) -> str:
    return password_hash.hash(plain_password)

def authentication_user(username: str, password: str):
    user = get_user(username)
    if not user:
        return False
    if not vertify_password(password, user.hashed_password):
        return False
    return user

async def get_current_user(token: str = Depends(oauth2_scheme)):
    pass