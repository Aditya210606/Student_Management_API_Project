from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.student import Student as StudentModel
from schemas.auth import StudentLogin
from core.security import verify_password, create_access_token


def student_login_service(form_data, db: Session):

    student = db.query(StudentModel).filter(
        StudentModel.email == form_data.username
    ).first()

    if not student:
        raise HTTPException( status_code=401,detail="Invalid credentials" )

    if not verify_password(form_data.password,student.password_hash):
        raise HTTPException( status_code=401, detail="Invalid credentials")

    access_token = create_access_token( {"sub": student.student_id,"role":"student"})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }