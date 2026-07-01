from fastapi import APIRouter, Depends
from schemas.departments import Department,DepartmentResponse,UpdateDepartment,SearchDepartment
from database.session import get_db
from sqlalchemy.orm import Session
from services.department_service import create_department_service , search_department_service ,view_all_department_service, view_particular_department_service,update_department_info_service,delete_department_service
from typing import List

router = APIRouter(prefix="/departments", tags=["departments"])

@router.post('/create')
def create_department(department:Department, db :Session = Depends(get_db)):
    return create_department_service(department, db)

@router.get('/',response_model=List[DepartmentResponse])
def view_all_department(db: Session = Depends(get_db)):
    return view_all_department_service(db)

@router.get('/search')
def search_department(filters:SearchDepartment = Depends(), db :Session = Depends(get_db)):
    return search_department_service(filters, db)

@router.get('/{department_id}',response_model=DepartmentResponse)
def view_particular_department(department_id : str, db: Session = Depends(get_db)):
    return view_particular_department_service(department_id, db)

@router.put('/{department_id}')
def update_department_info(department_id:str,update_department:UpdateDepartment, db: Session = Depends(get_db)):
    return update_department_info_service(department_id, update_department, db)

@router.delete('/{department_id}')
def delete_department(department_id: str , db:Session=Depends(get_db)):
    return delete_department_service(department_id, db)



