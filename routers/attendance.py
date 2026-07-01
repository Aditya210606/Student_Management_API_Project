from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database.session import get_db
from schemas.attendance import Attendance, SearchAttendance, UpdateAttendance, AttendanceResponse
from services.attendance_service import create_attendance_service , search_attendance_service ,view_all_attendance_service, view_particular_attendance_service,update_attendance_info_service,delete_attendance_service
from typing import List

router = APIRouter(prefix="/attendance", tags=["attendance"])

@router.post('/create')
def create_attendance(attendance:Attendance, db :Session = Depends(get_db)):
    return create_attendance_service(attendance, db)

@router.get('/',response_model=List[AttendanceResponse])
def view_all_attendance(db: Session = Depends(get_db)):
    return view_all_attendance_service(db)

@router.get('/search')
def search_attendance(filters:SearchAttendance = Depends(), db :Session = Depends(get_db)):
    return search_attendance_service(filters, db)

@router.get('/{attendance_id}',response_model=AttendanceResponse)
def view_particular_attendance(attendance_id : str, db: Session = Depends(get_db)):
    return view_particular_attendance_service(attendance_id, db)

@router.put('/{attendance_id}')
def update_attendance_info(attendance_id:str,update_attendance:UpdateAttendance, db: Session = Depends(get_db)):
    return update_attendance_info_service(attendance_id, update_attendance, db)

@router.delete('/{attendance_id}')
def delete_attendance(attendance_id: str , db:Session=Depends(get_db)):
    return delete_attendance_service(attendance_id, db)




