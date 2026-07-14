from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from schemas.auth import StudentLogin
from services.auth_service import student_login_service
from dependencies.auth import get_current_student
from models.student import Student as StudentModel
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/auth",tags=["Authentication"])


@router.post("/student/login")
def student_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return student_login_service(form_data, db)

@router.get("/student/me")
def get_student_profile(current_student: StudentModel = Depends(get_current_student)):
    return {
        "student_id": current_student.student_id,
        "first_name": current_student.first_name,
        "last_name": current_student.last_name,
        "email": current_student.email
    }