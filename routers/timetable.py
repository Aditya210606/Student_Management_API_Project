from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database.session import get_db
from schemas.timetable import  Timetable, SearchTimetable,UpdateTimetable, TimetableResponse
from services.timetable_service import create_timetable_service, search_timetable_service, view_all_timetable_service, view_particular_timetable_service, update_timetable_info_service, delete_timetable_service


router = APIRouter(prefix="/timetable", tags=["Timetable"])


@router.post("/create")
def create_timetable(timetable: Timetable, db: Session = Depends(get_db)):
    return create_timetable_service(timetable, db)


@router.get("/", response_model=List[TimetableResponse])
def view_all_timetable(db: Session = Depends(get_db)):
    return view_all_timetable_service(db)


@router.get("/search")
def search_timetable( filters: SearchTimetable = Depends(), db: Session = Depends(get_db)):
    return search_timetable_service(filters, db)


@router.get("/{timetable_id}", response_model=TimetableResponse)
def view_particular_timetable(timetable_id: str, db: Session = Depends(get_db)):
    return view_particular_timetable_service(timetable_id, db)


@router.put("/{timetable_id}")
def update_timetable_info(timetable_id: str, update_timetable: UpdateTimetable,db: Session = Depends(get_db)):
    return update_timetable_info_service( timetable_id, update_timetable, db )


@router.delete("/{timetable_id}")
def delete_timetable( timetable_id: str, db: Session = Depends(get_db)):
    return delete_timetable_service(timetable_id, db)