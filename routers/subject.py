from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database.session import get_db
from services.subject_service import create_subject_service
from schemas.subject import Subject
from typing import List

router = APIRouter(prefix="/subjects", tags=['subjects'])


@router.post('/create')
def create_subject(subject: List[Subject], db:Session = Depends(get_db)):
    return create_subject_service(subject, db)