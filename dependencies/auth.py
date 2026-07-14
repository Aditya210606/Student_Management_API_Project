from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from core.config import settings
from core.security import oauth2_scheme
from database.session import get_db
from models.student import Student as StudentModel


def get_current_student( token: str = Depends(oauth2_scheme),db: Session = Depends(get_db)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        student_id = payload.get("sub")
        role = payload.get("role")

        if student_id is None or role is None:
            raise credentials_exception

        if role != "student":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Student access required"
            )

    except JWTError:
        raise credentials_exception

    student = db.query(StudentModel).filter(
        StudentModel.student_id == student_id
    ).first()

    if student is None:
        raise credentials_exception

    return student