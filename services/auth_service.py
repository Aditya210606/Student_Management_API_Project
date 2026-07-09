from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.student import Student
from schemas.auth import LoginRequest
from core.security import verify_password


def student_login_service(login_data: LoginRequest, db: Session):

    # Step 1: Find student using email
    student = db.query(Student).filter(
        Student.email == login_data.email
    ).first()

    # Step 2: Check whether student exists
    if not student:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Step 3: Verify entered password with hashed password
    if not verify_password(
        login_data.password,
        student.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    # Temporary response
    return {
        "message": "Login successful",
        "student_id": student.student_id,
        "email": student.email
    }