from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from schemas.auth import LoginRequest
from services.auth_service import student_login_service


router = APIRouter(prefix="/auth",tags=["Authentication"])


@router.post("/student/login")
def student_login( login_data: LoginRequest, db: Session = Depends(get_db)):
    return student_login_service(login_data, db)