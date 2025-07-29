from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserCreate, UserResponse
from app.services.user_service import register_user, get_users
from app.db.session import get_db
from typing import List

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    pass

@router.get("/", response_model=List[UserResponse])
async def list_users(db: AsyncSession = Depends(get_db)):
    pass
