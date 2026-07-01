from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database.session import get_db
from services.subject_service import create_subject_service, view_all_subject_service,delete_subject_service,search_subject_service, view_particular_subject_service,update_subject_info_service
from schemas.subject import Subject, UpdateSubject, SearchSubject,SubjectResponse
from typing import List

router = APIRouter(prefix="/subjects", tags=['subjects'])


@router.post('/create')
def create_subject(subject: List[Subject], db:Session = Depends(get_db)):
    return create_subject_service(subject, db)

@router.get('/',response_model=List[SubjectResponse])
def view_all_subject(db:Session = Depends(get_db)):
    return view_all_subject_service(db)

@router.get('/search')
def search_subject(filters:SearchSubject = Depends(), db : Session = Depends(get_db)):
    return search_subject_service(filters, db)

@router.get('/{subject_id}', response_model=SubjectResponse)
def view_particular_subject(subject_id:str,db : Session = Depends(get_db)):
    return view_particular_subject_service(subject_id, db)

@router.put('/{subject_id}')
def update_subject_info(subject_id:str,updatesubject: UpdateSubject,db : Session = Depends(get_db)):
    return update_subject_info_service(subject_id,updatesubject, db)

@router.delete('/{subject_id}')
def delete_subject(subject_id:str,db : Session = Depends(get_db)):
    return delete_subject_service(subject_id, db)


