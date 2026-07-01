from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database.session import get_db
from schemas.marks import Marks, SearchMarks, UpdateMarks,  MarksResponse
from services.marks_service import create_marks_service , search_marks_service ,view_all_marks_service, view_particular_marks_service,update_marks_info_service,delete_marks_service
from typing import List

router = APIRouter(prefix="/marks", tags=["marks"])

@router.post('/create')
def create_marks(marks:Marks, db :Session = Depends(get_db)):
    return create_marks_service(marks, db)

@router.get('/',response_model=List[MarksResponse])
def view_all_marks(db: Session = Depends(get_db)):
    return view_all_marks_service(db)

@router.get('/search')
def search_marks(filters:SearchMarks = Depends(), db :Session = Depends(get_db)):
    return search_marks_service(filters, db)

@router.get('/{marks_id}',response_model=MarksResponse)
def view_particular_marks(marks_id : str, db: Session = Depends(get_db)):
    return view_particular_marks_service(marks_id, db)

@router.put('/{marks_id}')
def update_marks_info(marks_id:str,update_marks:UpdateMarks, db: Session = Depends(get_db)):
    return update_marks_info_service(marks_id, update_marks, db)

@router.delete('/{marks_id}')
def delete_attendance(marks_id: str , db:Session=Depends(get_db)):
    return delete_marks_service(marks_id, db)

