from fastapi import HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models.attendance import AttendanceModel
from schemas.attendance import Attendance, UpdateAttendance, SearchAttendance


def create_attendance_service(attendance: Attendance, db: Session):

    # Check if attendance already exists
    existing_attendance = db.query(AttendanceModel).filter( AttendanceModel.attendance_id == attendance.attendance_id).first()

    if existing_attendance:
        raise HTTPException(status_code=409, detail="Attendance already exists")

    # Create SQLAlchemy object
    new_attendance = AttendanceModel(
        attendance_id=attendance.attendance_id,
        student_id=attendance.student_id,
        subject_id=attendance.subject_id,
        teacher_id=attendance.teacher_id,
        attendance_date=attendance.attendance_date,
        lecture_number=attendance.lecture_number,
        status=attendance.status,
        remarks=attendance.remarks
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return JSONResponse(status_code=201,content={"message": "Attendance created successfully"})


def view_all_attendance_service(db: Session):

    attendance = db.query(AttendanceModel).all()

    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")

    return attendance


def search_attendance_service(filters: SearchAttendance, db: Session):

    total_attendance = db.query(AttendanceModel).count()

    # Base Query
    query = db.query(AttendanceModel)

    # ---------------- Filtering ----------------

    if filters.attendance_id:
        query = query.filter( AttendanceModel.attendance_id == filters.attendance_id )

    if filters.student_id:
        query = query.filter(AttendanceModel.student_id == filters.student_id)

    if filters.subject_id:
        query = query.filter( AttendanceModel.subject_id == filters.subject_id )

    if filters.teacher_id:
        query = query.filter(
            AttendanceModel.teacher_id == filters.teacher_id )

    if filters.attendance_date:
        query = query.filter( AttendanceModel.attendance_date == filters.attendance_date )

    if filters.lecture_number:
        query = query.filter( AttendanceModel.lecture_number == filters.lecture_number )

    if filters.status:
        query = query.filter( AttendanceModel.status == filters.status )

    filtered_attendance = query.count()

    # ---------------- Sorting ----------------

    if filters.sort_by:

        column = getattr(AttendanceModel, filters.sort_by)

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

    attendance = query.all()

    return {
        "total_attendance": total_attendance,
        "filtered_attendance": filtered_attendance,
        "page": page,
        "limit": limit,
        "attendance": attendance
    }


def view_particular_attendance_service(attendance_id: str, db: Session):

    particular_attendance = db.query(AttendanceModel).filter( AttendanceModel.attendance_id == attendance_id).first()

    if not particular_attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")

    return particular_attendance


def update_attendance_info_service(
    attendance_id: str,
    update_attendance: UpdateAttendance,
    db: Session
):

    existing_attendance = db.query(AttendanceModel).filter(
        AttendanceModel.attendance_id == attendance_id
    ).first()

    if not existing_attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")

    update_data = update_attendance.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(existing_attendance, key, value)

    db.commit()
    db.refresh(existing_attendance)

    return JSONResponse(
        status_code=200,
        content={"message": "Attendance updated successfully"}
    )


def delete_attendance_service(attendance_id: str, db: Session):

    attendance = db.query(AttendanceModel).filter(
        AttendanceModel.attendance_id == attendance_id
    ).first()

    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")

    db.delete(attendance)
    db.commit()

    return JSONResponse(
        status_code=200,
        content={"message": f"{attendance_id} attendance deleted successfully"}
    )