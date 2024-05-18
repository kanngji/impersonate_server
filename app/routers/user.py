from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from pymongo.collection import Collection
from app.db import client
from app.models.user import User
from app.schemas.user import UserCreate
from app.crud.user import create_user
from app.utils.security import hash_password

router = APIRouter()

# MongoDB database와 user collection 참조
db = client['your_database_name']
user_collection = db['users']

class UserSignUp(BaseModel):
    email: EmailStr
    password: str
    confirmPassword: str
    nickname: str

@router.post('/signup')
async def signup(user_data: UserSignUp):
    if user_data.password != user_data.confirmPassword:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    # 비밀번호 해싱
    hashed_password = hash_password(user_data.password)

    # 유저 객체 생성
    user = User(
        email=user_data.email,
        password=hashed_password,
        nickname=user_data.nickname
    )

    try:
        create_user(user_collection, user)
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
