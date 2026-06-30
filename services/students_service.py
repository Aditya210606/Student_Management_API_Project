from fastapi import HTTPException ,Depends, Path
from fastapi.responses import JSONResponse

from schemas.students import Student,StudentSearch,StudentResponse,UpdateStudent
from data import load_data, save_data
from sqlalchemy.orm import Session
from models.student import Student as StudentModel
from core.security import hash_password



def create_student_service(student: Student, db: Session):

    existing_student = ( db.query(StudentModel).filter(StudentModel.student_id == student.student_id).first() )

    if existing_student:
        raise HTTPException( status_code=409, detail="Student already exists" )

    new_student = StudentModel(
    student_id=student.student_id,
    first_name=student.first_name,
    last_name=student.last_name,
    email=student.email,
    phone_number=student.phone_number,
    age=student.age,
    gender=student.gender,
    admission_year=student.admission_year,
    year=student.year,
    cgpa=student.cgpa,
    city=student.city,
    department=student.department,
    password_hash=hash_password(student.password_hash),
    date_of_birth=student.date_of_birth,
    address=student.address,
    semester=student.semester
)

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return JSONResponse(status_code=201, content={"message": "Student created successfully"})

    # #data = load_data()
   
    # if student.student_id in db :
    #     raise HTTPException (status_code=409,detail="student already exist")
    
    # db[student.student_id] = student.model_dump()  #currently including the student_id in the data 

    # #save_data(data)

    # return JSONResponse(status_code=201,content={'message':'Student created successfully'})

def view_all_students_service(db: Session):
    #sql method 
    students = db.query(StudentModel).all()

    if not students :
        raise HTTPException (status_code=404, detail='students not found')
    return students 

# json method 
# data = load_data()
#   if data =={}:
#     raise HTTPException(status_code=404, detail='student not found')

def view_particular_student_service(student_id : str, db: Session ):

    student = db.query(StudentModel).filter(StudentModel.student_id == student_id).first()
    if not student :
        raise HTTPException (status_code=404, detail='Student not found')    
    
    return student

def update_student_info_service( student_id: str, update_student: UpdateStudent,  db: Session):
    # Find the student
    student = db.query(StudentModel).filter(StudentModel.student_id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Get only the fields sent by the client
    updated_data = update_student.model_dump(exclude_unset=True)

    # Update only those fields
    for key, value in updated_data.items():
        setattr(student, key, value)

    db.commit()
    db.refresh(student)

    return JSONResponse( status_code=200, content={"message": "Student updated successfully"})

    #json method 
    # data = load_data()

    # if student_id not in data:
    #     raise HTTPException(status_code=404, detail={"message": "Student not found"})

    # # Existing student data
    # existing_student_info = data[student_id]

    # # Only include fields sent by the client
    # updated_data = update_student.model_dump(exclude_unset=True)

    # # Update existing data
    # for key, value in updated_data.items():
    #     existing_student_info[key] = value

    # # Validate the final data
    # student_pydantic_obj = Student(**existing_student_info)

    # # Convert back to dictionary
    # data[student_id] = student_pydantic_obj.model_dump()

    # # Save to JSON
    # save_data(data)
    
    # return JSONResponse(status_code=200, content={'message':'Student info updated'})  # next the data is saved in the json file    

    
def search_students_service(filters: StudentSearch, db: Session ):

    # Total students before filtering
    total_students = db.query(StudentModel).count()

    # Base query
    query = db.query(StudentModel)

    # ---------------- Filtering ----------------

    if filters.student_id:
        query = query.filter(StudentModel.student_id == filters.student_id)

    if filters.first_name:
        query = query.filter( StudentModel.first_name.ilike(f"%{filters.first_name}%") )

    if filters.last_name:
        query = query.filter( StudentModel.last_name.ilike(f"%{filters.last_name}%") )

    if filters.email:
        query = query.filter( StudentModel.email.ilike(f"%{filters.email}%") )

    if filters.phone_number:
        query = query.filter( StudentModel.phone_number == filters.phone_number )

    if filters.age is not None:
        query = query.filter( StudentModel.age == filters.age)

    if filters.gender:
        query = query.filter( StudentModel.gender == filters.gender )

    if filters.city:
        query = query.filter( StudentModel.city.ilike(f"%{filters.city}%") )

    if filters.department:
        query = query.filter( StudentModel.department == filters.department )

    if filters.year is not None:
        query = query.filter( StudentModel.year == filters.year )

    if filters.admission_year is not None:
        query = query.filter( StudentModel.admission_year == filters.admission_year )

    if filters.cgpa is not None:
        query = query.filter( StudentModel.cgpa == filters.cgpa )

    if filters.min_cgpa is not None:
        query = query.filter( StudentModel.cgpa >= filters.min_cgpa )

    if filters.max_cgpa is not None:
        query = query.filter( StudentModel.cgpa <= filters.max_cgpa )

    # Count after filtering
    filtered_students = query.count()

    # ---------------- Sorting ----------------

    if filters.sort_by:

        column = getattr(StudentModel, filters.sort_by)

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
    students = query.all()

    return {
        "total_students": total_students,
        "filtered_students": filtered_students,
        "page": page,
        "limit": limit,
        "students": students
    }

    # data = load_data()

    # total_students = len(data)
    # result = []

    # # ---------------- Filtering ----------------

    # for student in data.values():

    #     if filters.city is not None and filter.city.lower() not in student["city"].lower():
    #         continue

    #     if filters.department is not None and student["department"] != filters.department:
    #         continue

    #     if filters.gender is not None and student["gender"] != filters.gender:
    #         continue

    #     if filters.year is not None and student["year"] != filters.year:
    #         continue

    #     if filters.admission_year is not None and student["admission_year"] != filters.admission_year:
    #         continue

    #     if filters.min_cgpa is not None and student["cgpa"] < filters.min_cgpa:
    #         continue

    #     if filters.max_cgpa is not None and student["cgpa"] > filters.max_cgpa:
    #         continue

    #     if filters.student_id is not None and student["student_id"] != filters.student_id:
    #         continue

    #     if filters.first_name is not None and filters.first_name.lower() not in student["first_name"].lower():
    #         continue

    #     if filters.last_name is not None and filters.last_name.lower() not in student["last_name"].lower():
    #         continue

    #     if filters.email is not None and filters.email.lower() not in student["email"].lower():
    #         continue

    #     if filters.phone_number is not None and student["phone_number"] != filters.phone_number:
    #         continue

    #     if filters.age is not None and student["age"] != filters.age:
    #         continue

    #     if filters.cgpa is not None and student["cgpa"] != filters.cgpa:
    #         continue

    #     result.append(student)

    # filtered_students = len(result)

    
    # # ---------------- Sorting ----------------

    # if filters.sort_by is not None:

    #     reverse = True if filters.sort_order == "desc" else False

    #     result = sorted(
    #         result,
    #         key=lambda student: student[filters.sort_by],
    #         reverse=reverse
    #     )


    # # ---------------- Pagination ----------------

    # if filters.page is not None and filters.limit is not None:

    #     start = (filters.page - 1) * filters.limit
    #     end = start + filters.limit

    #     result = result[start:end]

    #     return {
    #         "total_students": total_students,
    #         "filtered_students": filtered_students,
    #         "page":filters.page,
    #         "limit":filters.limit,
    #         "student": result
    #     }
   


  


def delete_student_service(student_id : str, db: Session):

    student = db.query(StudentModel).filter(StudentModel.student_id == student_id).first()

    if not student :
        raise HTTPException (status_code=404, detail="Student not found")
    
    db.delete(student)
    db.commit()

    return JSONResponse (status_code=200, content={'message':'Student deleted'})

    # data = load_data()

    # if student_id not in data :
    #     raise HTTPException (status_code=404, detail={'message':'student not found'})
    
    # del data[student_id]

    # save_data(data)

    # return JSONResponse(status_code=200, content={'message':'student deleted '})

