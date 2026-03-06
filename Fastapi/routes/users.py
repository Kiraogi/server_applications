from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

class User(BaseModel):
    name: str
    age: int
    email: str

@router.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@router.post("/users/")
def create_user(user: User):
    return {"message": f'Пользователь {user.name} создан!!!'}