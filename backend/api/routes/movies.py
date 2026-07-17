from fastapi import APIRouter, Depends, HTTPException, File, Form, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asynio import AsyncSession

router = APIRouter(prefix="/api/content", tags=["content"])

@router.get("/")
async def get_content(session: AsyncSession)