from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.timetable import TimetableModel
from schemas.timetable import Timetable, UpdateTimetable, SearchTimetable


def create_timetable_service(timetable: Timetable, db: Session):

    # Check if timetable already exists
    existing_timetable = db.query(TimetableModel).filter(
        TimetableModel.timetable_id == timetable.timetable_id ).first()

    if existing_timetable:
        raise HTTPException(status_code=409, detail="Timetable already exists")

    # Create SQLAlchemy object
    new_timetable = TimetableModel(
        timetable_id=timetable.timetable_id,
        department=timetable.department,
        semester=timetable.semester,
        section=timetable.section,
        subject_id=timetable.subject_id,
        teacher_id=timetable.teacher_id,
        day=timetable.day,
        lecture_number=timetable.lecture_number,
        start_time=timetable.start_time,
        end_time=timetable.end_time,
        classroom=timetable.classroom,
        academic_year=timetable.academic_year,
        is_active=timetable.is_active
    )

    db.add(new_timetable)
    db.commit()
    db.refresh(new_timetable)

    return JSONResponse( status_code=201, content={"message": "Timetable created successfully"} )


def view_all_timetable_service(db: Session):

    timetable = db.query(TimetableModel).all()

    if not timetable:
        raise HTTPException(status_code=404, detail="Timetable not found")

    return timetable


def search_timetable_service(filters: SearchTimetable, db: Session):

    total_timetable = db.query(TimetableModel).count()

    # Base Query
    query = db.query(TimetableModel)

    # ---------------- Filtering ----------------

    if filters.timetable_id:
        query = query.filter(TimetableModel.timetable_id == filters.timetable_id)

    if filters.department:
        query = query.filter(TimetableModel.department == filters.department)

    if filters.semester is not None:
        query = query.filter(TimetableModel.semester == filters.semester)

    if filters.section:
        query = query.filter(TimetableModel.section == filters.section)

    if filters.subject_id:
        query = query.filter(TimetableModel.subject_id == filters.subject_id)

    if filters.teacher_id:
        query = query.filter(TimetableModel.teacher_id == filters.teacher_id)

    if filters.day:
        query = query.filter(TimetableModel.day == filters.day)

    if filters.lecture_number is not None:
        query = query.filter(TimetableModel.lecture_number == filters.lecture_number)

    if filters.start_time:
        query = query.filter(TimetableModel.start_time == filters.start_time)

    if filters.end_time:
        query = query.filter(TimetableModel.end_time == filters.end_time)

    if filters.classroom:
        query = query.filter(TimetableModel.classroom == filters.classroom)

    if filters.academic_year:
        query = query.filter(TimetableModel.academic_year == filters.academic_year)

    if filters.is_active is not None:
        query = query.filter(TimetableModel.is_active == filters.is_active)

    filtered_timetable = query.count()

    # ---------------- Sorting ----------------

    if filters.sort_by:

        column = getattr(TimetableModel, filters.sort_by)

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

    timetable = query.all()

    return {
        "total_timetable": total_timetable,
        "filtered_timetable": filtered_timetable,
        "page": page,
        "limit": limit,
        "timetable": timetable
    }


def view_particular_timetable_service(timetable_id: str, db: Session):

    particular_timetable = db.query(TimetableModel).filter( TimetableModel.timetable_id == timetable_id ).first()

    if not particular_timetable:
        raise HTTPException(status_code=404, detail="Timetable not found")

    return particular_timetable


def update_timetable_info_service( timetable_id: str, update_timetable: UpdateTimetable, db: Session):

    existing_timetable = db.query(TimetableModel).filter( TimetableModel.timetable_id == timetable_id ).first()

    if not existing_timetable:
        raise HTTPException(status_code=404, detail="Timetable not found")

    update_data = update_timetable.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(existing_timetable, key, value)

    db.commit()
    db.refresh(existing_timetable)

    return JSONResponse( status_code=200, content={"message": "Timetable updated successfully"} )


def delete_timetable_service(timetable_id: str, db: Session):

    timetable = db.query(TimetableModel).filter( TimetableModel.timetable_id == timetable_id).first()

    if not timetable:
        raise HTTPException(status_code=404, detail="Timetable not found")

    db.delete(timetable)
    db.commit()

    return JSONResponse( status_code=200, content={"message": f"{timetable_id} timetable deleted successfully"} )