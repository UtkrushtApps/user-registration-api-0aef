from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserCreate
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from typing import List

async def register_user(user_in: UserCreate, db: AsyncSession):
    pass

async def get_users(db: AsyncSession):
    pass
