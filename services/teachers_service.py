from sqlalchemy.orm import Session
from models.teacher import TeacherModel
from fastapi import HTTPException  
from core.security import hash_password 
from fastapi.responses import JSONResponse
from schemas.teachers import UpdateTeacher,TeacherSearch

def create_teacher_service(teacher:TeacherModel, db:Session):

    existing_student =  db.query(TeacherModel).filter(TeacherModel.teacher_id == teacher.teacher_id).first() 

    if existing_student:
        raise HTTPException( status_code=409, detail="Student already exists" )
    
    new_teacher = TeacherModel(teacher_id=teacher.teacher_id,
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

def search_teacher_service(filters:TeacherSearch, db: Session):
    
    #total teacher before filtering 
    total_teacher = db.query(TeacherModel).count()

    #base query
    query = db.query(TeacherModel)

        # ---------------- Filtering ----------------

    if filters.teacher_id:
        query = query.filter(TeacherModel.teacher_id == filters.teacher_id)

    if filters.first_name:
        query = query.filter( TeacherModel.first_name.ilike(f"%{filters.first_name}%") )

    if filters.last_name:
        query = query.filter(TeacherModel.last_name.ilike(f"%{filters.last_name}%") )

    if filters.email:
        query = query.filter( TeacherModel.email.ilike(f"%{filters.email}%") )

    if filters.phone_number:
        query = query.filter( TeacherModel.phone_number == filters.phone_number )

    if filters.age is not None:
        query = query.filter( TeacherModel.age == filters.age)

    if filters.gender:
        query = query.filter(TeacherModel.gender == filters.gender )

    if filters.city:
        query = query.filter(TeacherModel.city.ilike(f"%{filters.city}%") )

    if filters.department:
        query = query.filter(TeacherModel.department == filters.department )

    if filters.designation:
        query = query.filter( TeacherModel.designation == filters.designation )

    if filters.qualification is not None:
        query = query.filter(TeacherModel.qualification == filters.qualification )

    if filters.experience is not None:
        query = query.filter(TeacherModel.experience == filters.max_experience )

    if filters.min_experience is not None:
        query = query.filter(TeacherModel.experience >= filters.min_experience )

    if filters.max_experience is not None:
        query = query.filter(TeacherModel.experience <= filters.max_experience )

    if filters.salary is not None:
        query = query.filter(TeacherModel.salary >= filters.salary )    

    if filters.min_salary is not None:
        query = query.filter(TeacherModel.salary >= filters.min_salary )

    if filters.max_salary is not None:
        query = query.filter(TeacherModel.salary <= filters.max_salary )

    if filters.joined_after:
        query = query.filter(TeacherModel.date_of_joining >= filters.joined_after)

    if filters.joined_before:
        query = query.filter(TeacherModel.date_of_joining <= filters.joined_before)  

    if filters.is_active:
        query = query.filter(TeacherModel.is_active <= filters.is_active) 

    if filters.is_verified:
        query = query.filter(TeacherModel.is_verified <= filters.is_verified) 

    # Count after filtering
    filtered_teacher = query.count()

    # ---------------- Sorting ----------------

    if filters.sort_by:

        column = getattr(TeacherModel, filters.sort_by)

        if filters.sort_order == "desc":
            query = query.order_by(column.desc())
        else:
            query = query.order_by(column.asc())

    # ---------------- Pagination ----------------

    # page = None
    # limit = None

    if filters.page is not None and filters.limit is not None:

        page = filters.page
        limit = filters.limit

        offset = (page - 1) * limit

        query = query.offset(offset).limit(limit)

    # Execute query
    teacher = query.all()

    return {
        "total_teacher": total_teacher,
        "filtered_teacher": filtered_teacher,
        "page": page,
        "limit": limit,
        "teacher": teacher
    }

def view_particular_teacher_service(teacher_id : str , db:Session):

    particular_teacher = db.query(TeacherModel).filter(TeacherModel.teacher_id==teacher_id).first()

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

    return JSONResponse(status_code=200, content={'message':f" {teacher_id} Teacher deleted"})

