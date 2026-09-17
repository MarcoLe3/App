import jwt
from fastapi import APIRouter, Depends
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
import asyncpg

from core import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from .sql_queries import FETCH_USER

router = APIRouter()
password_hash = PasswordHash()

class Token(BaseModel):
    access_token: str
    token_type: str

async def get_user(pool: asyncpg.Pool, username: str):
    async with pool.acquire() as connection:
        if user := await connection.fetch(FETCH_USER, username):
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