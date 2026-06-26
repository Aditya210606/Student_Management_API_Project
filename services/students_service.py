from fastapi import HTTPException ,Depends, Path
from fastapi.responses import JSONResponse

from models import Student,StudentSearch,StudentResponse,UpdateStudent
from data import load_data, save_data


def create_student_service(student: Student):
    data = load_data()
   
    if student.student_id in data :
        raise HTTPException (status_code=409,detail="student already exist")
    
    data[student.student_id] = student.model_dump()  #currently including the student_id in the data 

    save_data(data)

    return JSONResponse(status_code=201,content={'message':'Student created successfully'})

def view_all_students_service():
    data = load_data()

    if data == {} :
        
        return {'message :No students available'}
    return data


def search_students_service(filters: StudentSearch = Depends()):

    data = load_data()

    total_students = len(data)
    result = []

    # ---------------- Filtering ----------------

    for student in data.values():

        if filters.city is not None and filter.city.lower() not in student["city"].lower():
            continue

        if filters.department is not None and student["department"] != filters.department:
            continue

        if filters.gender is not None and student["gender"] != filters.gender:
            continue

        if filters.year is not None and student["year"] != filters.year:
            continue

        if filters.admission_year is not None and student["admission_year"] != filters.admission_year:
            continue

        if filters.min_cgpa is not None and student["cgpa"] < filters.min_cgpa:
            continue

        if filters.max_cgpa is not None and student["cgpa"] > filters.max_cgpa:
            continue

        if filters.student_id is not None and student["student_id"] != filters.student_id:
            continue

        if filters.first_name is not None and filters.first_name.lower() not in student["first_name"].lower():
            continue

        if filters.last_name is not None and filters.last_name.lower() not in student["last_name"].lower():
            continue

        if filters.email is not None and filters.email.lower() not in student["email"].lower():
            continue

        if filters.phone_number is not None and student["phone_number"] != filters.phone_number:
            continue

        if filters.age is not None and student["age"] != filters.age:
            continue

        if filters.cgpa is not None and student["cgpa"] != filters.cgpa:
            continue

        result.append(student)

    filtered_students = len(result)

    
    # ---------------- Sorting ----------------

    if filters.sort_by is not None:

        reverse = True if filters.sort_order == "desc" else False

        result = sorted(
            result,
            key=lambda student: student[filters.sort_by],
            reverse=reverse
        )


    # ---------------- Pagination ----------------

    if filters.page is not None and filters.limit is not None:

        start = (filters.page - 1) * filters.limit
        end = start + filters.limit

        result = result[start:end]

        return {
            "total_students": total_students,
            "filtered_students": filtered_students,
            "page":filters.page,
            "limit":filters.limit,
            "student": result
        }
def view_particular_student_service(student_id : str = Path(..., description='Student id of student', examples= ['S001'])):

    data = load_data()

    if student_id in data :

     student = StudentResponse(**data[student_id])
     return student
    raise HTTPException (status_code=404, detail='Student not found')    
    

def update_student_info_service(student_id: str, update_student: UpdateStudent):

    data = load_data()

    if student_id not in data:
        raise HTTPException(status_code=404, detail={"message": "Student not found"})

    # Existing student data
    existing_student_info = data[student_id]

    # Only include fields sent by the client
    updated_data = update_student.model_dump(exclude_unset=True)

    # Update existing data
    for key, value in updated_data.items():
        existing_student_info[key] = value

    # Validate the final data
    student_pydantic_obj = Student(**existing_student_info)

    # Convert back to dictionary
    data[student_id] = student_pydantic_obj.model_dump()

    # Save to JSON
    save_data(data)
    
    return JSONResponse(status_code=200, content={'message':'Student info updated'})  # next the data is saved in the json file    

def delete_student_service(student_id : str):

    data = load_data()

    if student_id not in data :
        raise HTTPException (status_code=404, detail={'message':'student not found'})
    
    del data[student_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'student deleted '})

