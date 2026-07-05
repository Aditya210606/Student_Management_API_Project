from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.marks import MarksModel
from schemas.marks import Marks, UpdateMarks, SearchMarks


def create_marks_service(marks: Marks, db: Session):

    # Check if marks already exist
    existing_marks = db.query(MarksModel).filter(
        MarksModel.mark_id == marks.mark_id
    ).first()

    if existing_marks:
        raise HTTPException(status_code=409, detail="Marks already exist")

    # Create SQLAlchemy object
    new_marks = MarksModel(
        mark_id=marks.mark_id,
        student_id=marks.student_id,
        subject_id=marks.subject_id,
        teacher_id=marks.teacher_id,
        internal_marks=marks.internal_marks,
        external_marks=marks.external_marks,
        practical_marks=marks.practical_marks,
        total_marks=marks.total_marks,
        grade=marks.grade,
        result=marks.result,
        remarks=marks.remarks
    )

    db.add(new_marks)
    db.commit()
    db.refresh(new_marks)

    return JSONResponse(
        status_code=201,
        content={"message": "Marks created successfully"}
    )


def view_all_marks_service(db: Session):

    marks = db.query(MarksModel).all()

    if not marks:
        raise HTTPException(status_code=404, detail="Marks not found")

    return marks


def search_marks_service(filters: SearchMarks, db: Session):

    total_marks = db.query(MarksModel).count()

    # Base Query
    query = db.query(MarksModel)

    # ---------------- Filtering ----------------

    if filters.mark_id:
        query = query.filter(MarksModel.mark_id == filters.mark_id)

    if filters.student_id:
        query = query.filter(MarksModel.student_id == filters.student_id)

    if filters.subject_id:
        query = query.filter(MarksModel.subject_id == filters.subject_id)

    if filters.teacher_id:
        query = query.filter(MarksModel.teacher_id == filters.teacher_id)

    if filters.internal_marks is not None:
        query = query.filter(MarksModel.internal_marks == filters.internal_marks)

    if filters.external_marks is not None:
        query = query.filter(MarksModel.external_marks == filters.external_marks)

    if filters.practical_marks is not None:
        query = query.filter(MarksModel.practical_marks == filters.practical_marks)

    if filters.total_marks is not None:
        query = query.filter(MarksModel.total_marks == filters.total_marks)

    if filters.grade:
        query = query.filter(MarksModel.grade == filters.grade)

    if filters.result:
        query = query.filter(MarksModel.result == filters.result)

    filtered_marks = query.count()

    # ---------------- Sorting ----------------

    if filters.sort_by:

        column = getattr(MarksModel, filters.sort_by)

        if filters.sort_order == "desc":
            query = query.order_by(column.desc())
        else:
            query = query.order_by(column.asc())

    # ---------------- Pagination ----------------

    if filters.page is not None and filters.limit is not None:

        page = filters.page
        limit = filters.limit

        offset = (page - 1) * limit

        query = query.offset(offset).limit(limit)

    marks = query.all()

    return {
        "total_marks": total_marks,
        "filtered_marks": filtered_marks,
        "page": page,
        "limit": limit,
        "marks": marks
    }


def view_particular_marks_service(mark_id: str, db: Session):

    particular_marks = db.query(MarksModel).filter( MarksModel.mark_id == mark_id).first()

    print(particular_marks.students.first_name)
    print(particular_marks.subject.subject_name)
    print(particular_marks.teacher.first_name)

    if not particular_marks:
        raise HTTPException(status_code=404, detail="Marks not found")

    return particular_marks


def update_marks_info_service( mark_id: str, update_marks: UpdateMarks, db: Session):

    existing_marks = db.query(MarksModel).filter( MarksModel.mark_id == mark_id).first()

    if not existing_marks:
        raise HTTPException(status_code=404, detail="Marks not found")

    update_data = update_marks.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(existing_marks, key, value)

    db.commit()
    db.refresh(existing_marks)

    return JSONResponse(
        status_code=200,
        content={"message": "Marks updated successfully"}
    )


def delete_marks_service(mark_id: str, db: Session):

    marks = db.query(MarksModel).filter(
        MarksModel.mark_id == mark_id
    ).first()

    if not marks:
        raise HTTPException(status_code=404, detail="Marks not found")

    db.delete(marks)
    db.commit()

    return JSONResponse(
        status_code=200,
        content={"message": f"{mark_id} marks deleted successfully"}
    )