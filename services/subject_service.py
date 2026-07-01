from sqlalchemy.orm import Session
from models.subject import SubjectModel
from schemas.subject import Subject
from fastapi import HTTPException

def create_subject_service(subject:SubjectModel ,db:Session):
    existing_subject = db.query(SubjectModel).filter(SubjectModel.subject_id==subject.subject_id).first()

    if existing_subject :
        raise HTTPException (status_code=409, detail="Subject already exists")
    
    new_subject = SubjectModel(
        subject_id=Subject.subject_id,
        subject_name=Subject.subject_name,
        subject_code=Subject.subject_code,
        department=Subject.department,
        semester=Subject.semester,
        credits=Subject.credits,
        subject_type=Subject.subject_type,
        teacher_id=Subject.teacher_id,
        description=Subject.description,
        is_active=Subject.is_active
    )

    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)