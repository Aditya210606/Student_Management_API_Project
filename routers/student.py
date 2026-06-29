from fastapi import APIRouter, HTTPException, Depends, Path
from fastapi.responses import JSONResponse
from schemas.students import Student,StudentSearch,StudentResponse,UpdateStudent
from data import load_data, save_data
from services.students_service import create_student_service,view_all_students_service,search_students_service,view_particular_student_service,update_student_info_service, delete_student_service
from sqlalchemy.orm import Session
from database.session import get_db
router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/create")
def create_student(student: Student , db :Session = Depends(get_db)):
   return create_student_service(student, db)

# endpoint for viewing all the students in the students.json file 

@router.get('/')
def view_all_students( db : Session = Depends(get_db)):
    return view_all_students_service(db)


@router.get("/search")
def search_students(filters: StudentSearch = Depends(), db : Session =Depends(get_db)):
    return search_students_service(filters,db)

    
# this is the endpoint for viewing a particular student detail
@router.get('/{student_id}',response_model=StudentResponse)
def view_particular_student( student_id : str, db : Session = Depends(get_db)):
    return view_particular_student_service(student_id, db)
           
# endpoint for updating the student information

@router.put("/{student_id}")
def update_student_info(student_id: str, update_student: UpdateStudent, db : Session = Depends(get_db)):
    return update_student_info_service(student_id,update_student,db)


@router.delete('/{student_id}')
def delete_student(student_id : str, db: Session= Depends(get_db)):
    return delete_student_service(student_id,db)



  
   





