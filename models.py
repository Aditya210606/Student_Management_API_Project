from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,Literal,Optional

class Student(BaseModel):

    student_id : Annotated[str, Field(...,description="Id of student",examples=["S001","S002"])]
    first_name : Annotated[str, Field(...,description="Student's first name", min_length= 2, max_length=30)]
    last_name :  Annotated[str, Field(...,description="Student's last name", min_length= 2, max_length=30)]
    email : Annotated[EmailStr, Field(...,description="Student's email address")]
    phone_number : Annotated[str, Field(...,min_length= 10, max_length= 10, description="Exactly 10 digit phone no.", examples=['9028594749'])]
    age :Annotated[int, Field(...,ge = 17, le = 30,description="Age of the student")]
    gender : Annotated[Literal["Male","Female","other"], Field(...,description="Gender of the student")] 
    year : Annotated[Literal[1,2,3,4], Field(..., description="Student year of study")]
    cgpa : Annotated[float, Field(...,ge = 0, le = 10, description="CGPA in range 0 to 10")]
    city : Annotated[str, Field(...,description="City of student living", min_length=2,max_length=30)]
    department: Annotated[Literal[ "AI&DS", "CSE", "IT", "EXTC", "Mechanical", "Civil" ], Field(...,description="Department of the student")]

class UpdateStudent(BaseModel):  

    student_id : Annotated[Optional[str], Field(description="Id of student",examples=["S001","S002"])]
    first_name : Annotated[Optional[str], Field(description="Student's first name", min_length= 2, max_length=30)]
    last_name :  Annotated[Optional[str], Field(description="Student's last name", min_length= 2, max_length=30)]
    email : Annotated[Optional[EmailStr], Field(description="Student's email address")]
    phone_number : Annotated[Optional[str], Field(min_length= 10, max_length= 10, description="Exactly 10 digit phone no.", examples=['9028594749'])]
    age :Annotated[Optional[int], Field(...,ge = 17, le = 30,description="Age of the student")]
    gender : Annotated[Optional[Literal["Male","Female","other"]], Field(description="Gender of the student")] 
    year : Annotated[Optional[Literal[1,2,3,4]], Field( description="Student year of study")]
    cgpa : Annotated[Optional[float], Field(...,ge = 0, le = 10, description="CGPA in range 0 to 10")]
    city : Annotated[Optional[str], Field(description="City of student living", min_length=2,max_length=30)]
    department: Annotated[Optional[Literal[ "AI&DS", "CSE", "IT", "EXTC", "Mechanical", "Civil" ]], Field(description="Department of the student")]  