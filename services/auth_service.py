from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.student import Student
from schemas.auth import StudentLogin
from core.security import verify_password, create_access_token


def student_login_service(login_data: StudentLogin, db: Session):

    # Step 1: Find student in database
    student = (
        db.query(Student)
        .filter(Student.student_id == login_data.student_id)
        .first()
    )

    # Step 2: Check whether student exists
    if not student:
        raise HTTPException(
            status_code=401,
            detail="Invalid student ID or password"
        )

    # Step 3: Verify entered password against stored hash
    if not verify_password(
        login_data.password,
        student.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid student ID or password"
        )

    # Step 4: Create JWT access token
    access_token = create_access_token(
        data={
            "sub": student.student_id
        }
    )

    # Step 5: Return token
    return {
    "message": "Login successful",
    "access_token": access_token,
    "token_type": "bearer",
    "student_id": student.student_id,
    "email": student.email
}