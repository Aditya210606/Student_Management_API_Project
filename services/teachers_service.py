from sqlalchemy.orm import Session
from models.teacher import TeacherModel
from fastapi import HTTPException  
from core.security import hash_password 
from fastapi.responses import JSONResponse
from schemas.teachers import UpdateTeacher




def create_teacher_service(teacher:TeacherModel, db:Session):

    existing_student = ( db.query(TeacherModel).filter(TeacherModel.teacher_id == teacher.teacher_id).first() )

    if existing_student:
        raise HTTPException( status_code=409, detail="Student already exists" )
    
    new_teacher = TeacherModel(
    teacher_id=teacher.teacher_id,
    first_name=teacher.first_name,
    last_name=teacher.last_name,
    email=teacher.email,
    phone_number=teacher.phone_number,
    password_hash=hash_password(teacher.password_hash),
    age=teacher.age,
    gender=teacher.gender,
    date_of_birth=teacher.date_of_birth,
    city=teacher.city,
    address=teacher.address,
    department=teacher.department,
    designation=teacher.designation,
    qualification=teacher.qualification,
    experience=teacher.experience,
    salary=teacher.salary,
    date_of_joining=teacher.date_of_joining,
    is_verified=teacher.is_verified,
    is_active=teacher.is_active,
    profile_image=teacher.profile_image
)

    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return JSONResponse(status_code=201, content={'message':'Teacher added successfully'})


def view_all_teacher_service(db:Session):
    
   teachers = db.query(TeacherModel).all()

   if not teachers:
       raise HTTPException(status_code=404, detail="Teachers not found")
   return teachers
  

def view_particular_teacher_service(teacher_id : str , db:Session):

    particular_teacher = db.query(TeacherModel).filter(TeacherModel.teacher_id == teacher_id).first()

    if not particular_teacher :
        raise HTTPException (status_code=404, detail="Teacher not found")
    return particular_teacher


def update_teacher_info_service(teacher_id : str , update_teacher: UpdateTeacher,db:Session ):

    existing_teacher = db.query(TeacherModel).filter(TeacherModel.teacher_id==teacher_id).first()

    if not existing_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    update_data = update_teacher.model_dump(exclude_unset=True)

    for key,value in update_data.items():
        setattr(existing_teacher, key , value)

    db.commit()
    db.refresh(existing_teacher)

    return JSONResponse(status_code=200, content={'message':'Teacher updated successfully'})  


def delete_teacher_service(teacher_id:str, db:Session):
    teacher = db.query(TeacherModel).filter(TeacherModel.teacher_id==teacher_id).first()

    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    
    db.delete(teacher)
    db.commit()

    return JSONResponse(status_code=200, content={'message':f'{teacher_id} Teacher deleted'})



   


    
