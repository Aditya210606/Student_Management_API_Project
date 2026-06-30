from fastapi import APIRouter, Depends
from schemas.teachers import Teacher,TeacherResponse,TeacherSearch,UpdateTeacher
from database.session import get_db
from sqlalchemy.orm import Session
from services.teachers_service import create_teacher_service,view_all_teacher_service, view_particular_teacher_service,update_teacher_info_service,delete_teacher_service,search_teacher_service


router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.post('/create')
def create_teacher(teacher:Teacher, db :Session = Depends(get_db)):
    return create_teacher_service(teacher, db)

@router.get('/')
def view_all_teacher(db: Session = Depends(get_db)):
    return view_all_teacher_service(db)

@router.get('/search')
def search_teacher(filters:TeacherSearch = Depends(), db :Session = Depends(get_db)):
    return search_teacher_service(filters, db)

@router.get('/{teacher_id}',response_model=TeacherResponse)
def view_particular_teacher(teacher_id : str, db: Session = Depends(get_db)):
    return view_particular_teacher_service(teacher_id, db)


@router.put('/{teacher_id}')
def update_teacher_info(teacher_id:str,update_teacher:UpdateTeacher, db: Session = Depends(get_db)):
    return update_teacher_info_service(teacher_id, update_teacher, db)

@router.delete('/{teacher_id}')
def delete_teacher(teacher_id: str , db:Session=Depends(get_db)):
    return delete_teacher_service(teacher_id, db)



