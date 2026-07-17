from fastapi import APIRouter, Depends, HTTPException, File, Form, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asynio import AsyncSession
from db.database import get_movies_db

router = APIRouter(prefix="/api/content", tags=["content"])

@router.get("/content")
async def get_content(db: AsyncSession = Depends(get_movies_db)):
    return get_movies_db(db)