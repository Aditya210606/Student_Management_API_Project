from fastapi import FastAPI, HTTPException, Path
from fastapi.responses import JSONResponse
from models import Student,UpdateStudent
from data import load_data, save_data

app = FastAPI()

# endpoint created for creating a student in the students.json file 

@app.post("/create")
def create_student(student: Student):
    data = load_data()
   
    if student.student_id in data :
        raise HTTPException (status_code=409,detail="student already exist")
    
    data[student.student_id] = student.model_dump()  #currently including the student_id in the data 

    save_data(data)

    return JSONResponse(status_code=201,content={'message':'Student created successfully'})

# endpoint for viewing all the students in the students.json file 

@app.get('/students')
def view_all_students():
    data = load_data()

    if data == {} :
        return {'message :No students available'}
    return data
  
# this is the endpoint for viewing a particular student detail

@app.get('/students/{student_id}')
def view_particular_student(student_id : str = Path(..., description='Student id of student', examples= ['S001'])):

    data = load_data()

    if student_id in data :
        return data[student_id]
    raise HTTPException (status_code=404, detail='Student not found')
    
# endpoint for updating the student information

@app.put('/students/{student_id}')
def update_student_info(student_id:str , update_student : UpdateStudent):

    data = load_data()

    if student_id not in data :
        raise HTTPException (status_code=404, detail={'message':'Student not found'})

    existing_student_info = data[student_id]      #current existing student data stored in existing student info

    updated_data = update_student.model_dump(exclude_unset=True)  #updated data is stored in updated_data and convert data into dictionary 

    for key,value in updated_data.items():                # replaces the value of existing data from the updated data 
        existing_student_info[key] = value

    student_pydantic_obj = Student(**existing_student_info)  # now the dictonary is stored in object to check the validation from student model

    existing_student_info = student_pydantic_obj.model_dump()   # after checking the existing info is again stord in dict 
 
    data[student_id] = existing_student_info  # the data is stored in the specific student_id 

    save_data(data)
    
    return JSONResponse(status_code=200, content={'message':'Student info updated'})  # next the data is saved in the json file 

# this endpoint is to delete the existing student in the json data

@app.delete('/students/{student_id}')
def delete_student(student_id : str):

    data = load_data()

    if student_id not in data :
        raise HTTPException (status_code=404, detail={'message':'student not found'})
    
    del data[student_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'student deleted '})








    


