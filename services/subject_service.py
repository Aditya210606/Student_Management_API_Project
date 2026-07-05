from sqlalchemy.orm import Session
from models.subject import SubjectModel
from schemas.subject import Subject, UpdateSubject,SearchSubject
from fastapi import HTTPException
from fastapi.responses import JSONResponse


def create_subject_service(subjects: list[Subject], db: Session):

    created_subjects = 0
    skipped_subjects = []

    for subject in subjects:

        existing_subject = db.query(SubjectModel).filter(
            SubjectModel.subject_id == subject.subject_id
        ).first()

        if existing_subject:
            skipped_subjects.append(subject.subject_id)
            continue

        new_subject = SubjectModel(
            subject_id=subject.subject_id,
            subject_name=subject.subject_name,
            subject_code=subject.subject_code,
            department_id=subject.department_id,
            semester=subject.semester,
            credits=subject.credits,
            subject_type=subject.subject_type,
            teacher_id=subject.teacher_id,
            description=subject.description,
            is_active=subject.is_active
        )

        db.add(new_subject)
        created_subjects += 1

    db.commit()

    return {
        "message": "Subjects inserted successfully.",
        "created_subjects": created_subjects,
        "skipped_subjects": skipped_subjects
    }


def view_all_subject_service(db:Session):

    existing_subject = db.query(SubjectModel).all()

    if not existing_subject:
        raise HTTPException(status_code=404, detail="No Subjects found")
    
    return existing_subject

def view_particular_subject_service(subject_id: str , db :Session):

    existing_subject = db.query(SubjectModel).filter(SubjectModel.subject_id == subject_id).first()

    print(existing_subject.teacher.teacher_id)
    print(existing_subject.teacher.first_name)
    print(existing_subject.teacher.last_name)

    if not existing_subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    
    return existing_subject

def update_subject_info_service(subject_id : str , updatesubject : UpdateSubject, db:Session):

    existing_subject = db.query(SubjectModel).filter(SubjectModel.subject_id == subject_id).first()

    if not existing_subject:
        raise HTTPException (status_code=404, detail="Subject not found")
    
    updated_data = updatesubject.model_dump(exclude_unset=True)

    for key,value in updated_data.items():
      setattr(existing_subject, key , value)

    db.commit()
    db.refresh(existing_subject)

    return JSONResponse(status_code=201, content={'message':'Subject updated successfully'})



def search_subject_service(filters: SearchSubject, db: Session):

    query = db.query(SubjectModel)

    total_subjects = query.count()

    # ---------------- Filtering ----------------

    if filters.subject_id is not None:
        query = query.filter( SubjectModel.subject_id == filters.subject_id )

    if filters.subject_name is not None:
        query = query.filter( SubjectModel.subject_name.ilike(f"%{filters.subject_name}%"))

    if filters.subject_code is not None:
        query = query.filter( SubjectModel.subject_code.ilike(f"%{filters.subject_code}%") )

    if filters.department_id is not None:
        query = query.filter( SubjectModel.department == filters.department.id )

    if filters.semester is not None:
        query = query.filter( SubjectModel.semester == filters.semester)

    if filters.credits is not None:
        query = query.filter( SubjectModel.credits == filters.credits)

    if filters.subject_type is not None:
        query = query.filter( SubjectModel.subject_type == filters.subject_type)

    if filters.teacher_id is not None:
        query = query.filter( SubjectModel.teacher_id == filters.teacher_id)

    if filters.is_active is not None:
        query = query.filter(SubjectModel.is_active == filters.is_active )

    filtered_subjects = query.count()

    # ---------------- Sorting ----------------

    if filters.sort_by is not None:

        column = getattr(SubjectModel, filters.sort_by)

        if filters.sort_order == "desc":
            query = query.order_by(column.desc())
        else:
            query = query.order_by(column.asc())

    # ---------------- Pagination ----------------

    if filters.page is not None and filters.limit is not None:

        start = (filters.page - 1) * filters.limit

        query = query.offset(start).limit(filters.limit)

    subjects = query.all()

    return {
        "total_subjects": total_subjects,
        "filtered_subjects": filtered_subjects,
        "page": filters.page,
        "limit": filters.limit,
        "subjects": subjects
    }

def delete_subject_service(subject_id:str, db:Session):

    subject = db.query(SubjectModel).filter(SubjectModel.subject_id == subject_id).first()

    if not subject :
        raise HTTPException (status_code=404, detail="Subject not found")
    
    db.delete(subject)
    db.commit()

    return JSONResponse (status_code=200, content={'message':'Subject deleted'})