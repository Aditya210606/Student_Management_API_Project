from pydantic import BaseModel,Field,EmailStr, computed_field,field_validator,model_validator
from typing import Annotated,Literal,Optional
from datetime import date

class Student(BaseModel):

    student_id : Annotated[str, Field(...,description="Id of student",examples=["S001","S002"])]
    first_name : Annotated[str, Field(...,description="Student's first name", min_length= 2, max_length=30)]
    last_name :  Annotated[str, Field(...,description="Student's last name", min_length= 2, max_length=30)]
    email : Annotated[EmailStr, Field(...,description="Student's email address")]
    phone_number : Annotated[str, Field(...,min_length= 10, max_length= 10, description="Exactly 10 digit phone no.", examples=['9028594749'])]
    age :Annotated[int, Field(...,ge = 17, le = 30,description="Age of the student")]
    gender : Annotated[Literal["Male","Female","other"], Field(...,description="Gender of the student")] 
    admission_year : Annotated[int , Field(...,description='Year of admission')]
    year : Annotated[Literal[1,2,3,4], Field(..., description="Student year of study")]
    cgpa : Annotated[float, Field(...,ge = 0, le = 10, description="CGPA in range 0 to 10")]
    city : Annotated[str, Field(...,description="City of student living", min_length=2,max_length=30)]
    department: Annotated[Literal[ "AI&DS", "CSE", "IT", "EXTC", "Mechanical", "Civil" ], Field(...,description="Department of the student")]
    password_hash: Annotated[ str,Field(..., min_length=6, description="Student password")]
    date_of_birth: date
    address: Annotated[str, Field(..., min_length=3)]
    semester: Annotated[int,Field(..., ge=1, le=8)]



    @field_validator('student_id')
    @classmethod
    def validate_student_id( cls , value):
       if not value.startswith("S"):
        raise ValueError("Student ID must start with 'S'")
       return value  
       
    @field_validator('phone_number')
    @classmethod
    def validate_phone_number(cls, value):
       if value.isdigit():
          return value
       raise ValueError("Invalid phone number")

    @field_validator("city")
    @classmethod
    def validate_city(cls, value):
     return value.title()
    
 
    @model_validator(mode="after")
    def validate_student(self):
       if self.age == 17 and self.year in [3,4]:
             raise ValueError ("Student not eligible")
       return self
 #-----------------------------------------------------------------------------------------------------------------------------------------------

class UpdateStudent(BaseModel):  

    student_id: Annotated[Optional[str], Field(description="Id of student", examples=["S001", "S002"])] = None
    first_name: Annotated[Optional[str], Field(description="Student's first name", min_length=2, max_length=30)] = None
    last_name: Annotated[Optional[str], Field(description="Student's last name", min_length=2, max_length=30)] = None
    email: Annotated[Optional[EmailStr], Field(description="Student's email address")] = None
    phone_number: Annotated[Optional[str], Field(min_length=10, max_length=10, description="Exactly 10 digit phone no.", examples=["9028594749"])] = None
    age: Annotated[Optional[int], Field(ge=17, le=30, description="Age of the student")] = None
    gender: Annotated[Optional[Literal["Male", "Female", "other"]], Field(description="Gender of the student")] = None
    admission_year: Annotated[Optional[int], Field(description="Year of admission")] = None
    year: Annotated[Optional[Literal[1, 2, 3, 4]], Field(description="Student year of study")] = None
    cgpa: Annotated[Optional[float], Field(ge=0, le=10, description="CGPA in range 0 to 10")] = None
    city: Annotated[Optional[str], Field(description="City of student living", min_length=2, max_length=30)] = None
    department: Annotated[ Optional[ Literal["AI&DS", "CSE", "IT", "EXTC", "Mechanical", "Civil"] ], Field(description="Department of the student")] = None
    password_hash: Annotated[Optional[str], Field(min_length=6, description="Student password")] = None
    date_of_birth: Optional[date] = None
    address: Annotated[ Optional[str], Field(min_length=10)] = None
    semester: Annotated[ Optional[int], Field(ge=1, le=8)]
#-------------------------------------------------------------------------

class StudentResponse(Student):

 @computed_field
 @property
 def full_name(self) -> str :

    full_name = self.first_name + ' ' + self.last_name

    return full_name
 
  
 
 #--------------------------------------------------------------------------

class StudentSearch(BaseModel):

    student_id: Annotated[ Optional[str],  Field(description="Id of student", examples=["S001", "S002"])] = None
    first_name: Annotated[ Optional[str], Field(description="Student's first name", min_length=2, max_length=30)] = None
    last_name: Annotated[ Optional[str], Field(description="Student's last name", min_length=2, max_length=30)] = None
    email: Annotated[ Optional[EmailStr], Field(description="Student's email address")] = None
    phone_number: Annotated[ Optional[str],Field( min_length=10, max_length=10, description="Exactly 10 digit phone no.", examples=["9028594749"])] = None
    age: Annotated[Optional[int], Field(ge=17, le=30, description="Age of the student") ] = None
    gender: Annotated[ Optional[Literal["Male", "Female", "other"]], Field(description="Gender of the student")] = None
    admission_year: Annotated[ Optional[int], Field(description="Year of admission") ] = None
    year: Annotated[ Optional[Literal[1, 2, 3, 4]], Field(description="Student year of study") ] = None
    cgpa: Annotated[ Optional[float],Field(ge=0, le=10, description="Exact CGPA") ] = None
    city: Annotated[Optional[str], Field(description="City of student living", min_length=2, max_length=30) ] = None
    department: Annotated[Optional[ Literal[ "AI&DS", "CSE", "IT", "EXTC", "Mechanical", "Civil"  ] ], Field(description="Department of the student")] = None
    date_of_birth: Optional[date] = None
    address: Annotated[ Optional[str], Field(min_length=10, description="Student address")] = None
    semester: Annotated[ Optional[int],Field(ge=1, le=8, description="Semester")] = None
    # ---------- Range Filters ----------
    min_cgpa: Annotated[ Optional[float],Field(ge=0, le=10, description="Minimum CGPA")] = None
    max_cgpa: Annotated[ Optional[float],Field(ge=0, le=10, description="Maximum CGPA")] = None
    # ---------- Sorting ---------
    sort_by: Annotated[Optional[ Literal[ "first_name", "last_name","cgpa","age", "year", "city","admission_year","semester" ]],Field(description="Field used for sorting")] = None
    sort_order: Annotated[ Optional[Literal["asc", "desc"]],Field(description="Sorting order")] = "asc"
    # ---------- Pagination ----------
    page: Annotated[  int, Field(ge=1, description="Page number") ] = 1
    limit: Annotated[ int,Field(ge=1, le=100, description="Records per page")] = 10