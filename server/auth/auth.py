import jwt
from fastapi import APIRouter, Depends, HTTPException, Header, status
from pwdlib import PasswordHash
from datetime import datetime, timedelta, timezone
from typing import Annotated
from pydantic import BaseModel

router = APIRouter()
password_hash = PasswordHash()

SECRET_KEY = "22cda67d26b53198335fcca6297016c8235a1cd39d51576e64a46d495a0f1fb2"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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

@router.get("/auth/token")
async def login_for_access_token(user_header: Annotated[str, Header()]) -> Token:
    user = authentication_user(username, password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.id}, expires_delta=access_token_expire
    )
    return Token(access_token=access_token, token_type="bearer")