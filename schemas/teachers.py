from datetime import date
from typing import Annotated, Literal,Optional
from pydantic import BaseModel, EmailStr, Field,computed_field


class Teacher(BaseModel):

    teacher_id: Annotated[ str,Field( ..., description="Unique Teacher ID", examples=["T001"])]

    first_name: Annotated[ str,Field( ...,min_length=2, max_length=30,description="Teacher's first name")]

    last_name: Annotated[str, Field( ..., min_length=2, max_length=30, description="Teacher's last name" )]

    email: Annotated[ EmailStr, Field( ..., description="Teacher email address" ) ]

    phone_number: Annotated[ str,Field(..., min_length=10, max_length=10, description="10 digit mobile number", examples=["9876543210"] )]

    password_hash: Annotated[str, Field( ..., min_length=6, max_length=100, description="Teacher password" )]

    age: Annotated[int, Field( ..., ge=22, le=70, description="Teacher age" )]

    gender: Annotated[Literal["Male", "Female", "Other"], Field(..., description="Teacher gender" )]

    date_of_birth: Annotated[ date,Field( ..., description="Teacher Date of Birth")]

    city: Annotated[str, Field( ...,min_length=2, max_length=30, description="City")]

    address: Annotated[ str, Field( ..., min_length=10, max_length=255, description="Residential Address" ) ]

    department: Annotated[ Literal[ "AI&DS", "CSE", "IT", "EXTC", "Mechanical", "Civil",  "Electronics", "Electrical" ], Field( ...,description="Department") ]

    designation: Annotated[ Literal[ "Assistant Professor", "Associate Professor", "Professor", "Head of Department", "Dean", "Principal" ], Field( ..., description="Teacher designation" ) ]

    qualification: Annotated[Literal["B.E", "B.Tech", "M.E","M.Tech","M.Sc","PhD"],Field(  ...,  description="Highest Qualification" )]

    experience: Annotated[ int, Field( ..., ge=0, le=50, description="Teaching experience in years" ) ]

    salary: Annotated[ float,Field( ..., ge=10000, le=1000000, description="Monthly salary" )]

    date_of_joining: Annotated[date,Field( ..., description="Joining Date" )]

    is_verified: Annotated[ bool, Field( default=False, description="Verification Status" )]

    is_active: Annotated[ bool, Field( default=True, description="Account Status" )]

    profile_image: Annotated[ str, Field( default="default_teacher.png", description="Profile image filename" )]



class UpdateTeacher(BaseModel):

    teacher_id: Annotated[ Optional[str], Field(description="Unique Teacher ID", examples=["T001"])] = None

    first_name: Annotated[ Optional[str], Field(description="Teacher's first name", min_length=2, max_length=30)] = None

    last_name: Annotated[ Optional[str], Field(description="Teacher's last name", min_length=2, max_length=30)] = None

    email: Annotated[ Optional[EmailStr], Field(description="Teacher email address")] = None

    phone_number: Annotated[ Optional[str], Field( min_length=10, max_length=10, description="10 digit mobile number", examples=["9876543210"] )] = None

    password_hash: Annotated[ Optional[str], Field( min_length=6, description="Hashed password" ) ] = None

    age: Annotated[ Optional[int], Field( ge=22, le=70, description="Teacher age" )] = None

    gender: Annotated[ Optional[Literal["Male", "Female", "Other"]], Field(description="Teacher gender")] = None

    date_of_birth: Optional[date] = None

    city: Annotated[ Optional[str], Field( min_length=2, max_length=30, description="City" )] = None

    address: Annotated[ Optional[str], Field( min_length=10, max_length=255, description="Residential Address" )] = None

    department: Annotated[ Optional[ Literal[ "AI&DS", "CSE","IT", "EXTC" "Mechanical", "Civil", "Electronics","Electrical" ] ], Field(description="Department")] = None

    designation: Annotated[ Optional[ Literal[ "Assistant Professor", "Associate Professor", "Professor", "Head of Department", "Dean", "Principal" ] ], Field(description="Teacher designation")] = None

    qualification: Annotated[ Optional[Literal[ "B.E", "B.Tech", "M.E", "M.Tech", "M.Sc", "PhD" ]], Field(description="Highest Qualification")] = None

    experience: Annotated[ Optional[int], Field( ge=0, le=50, description="Teaching experience in years" )] = None

    salary: Annotated[ Optional[float], Field( ge=10000, le=1000000, description="Monthly salary" ) ] = None

    date_of_joining: Optional[date] = None 

    profile_image: Annotated[ Optional[str],Field(description="Profile image filename")] = None


class TeacherSearch(BaseModel):

    teacher_id: Annotated[ Optional[str], Field(description="Teacher ID", examples=["T001"])] = None

    first_name: Annotated[Optional[str], Field(description="Teacher's first name", min_length=2, max_length=30)] = None

    last_name: Annotated[ Optional[str], Field(description="Teacher's last name", min_length=2, max_length=30) ] = None

    email: Annotated[ Optional[EmailStr], Field(description="Teacher email address") ] = None

    phone_number: Annotated[ Optional[str], Field( min_length=10, max_length=10, description="Teacher phone number", examples=["9876543210"] )] = None

    age: Annotated[ Optional[int], Field(ge=22, le=70, description="Teacher age")] = None

    gender: Annotated[ Optional[Literal["Male", "Female", "Other"]], Field(description="Teacher gender")] = None

    city: Annotated[ Optional[str], Field(min_length=2, max_length=30, description="City") ] = None

    department: Annotated[ Optional[ Literal[ "AI&DS", "CSE", "IT", "EXTC", "Mechanical", "Civil", "Electronics", "Electrical" ] ], Field(description="Department")] = None

    designation: Annotated[ Optional[ Literal[ "Assistant Professor", "Associate Professor", "Professor", "Head of Department", "Dean", "Principal" ] ], Field(description="Teacher designation") ] = None

    qualification: Annotated[ Optional[ Literal[ "B.E", "B.Tech", "M.E", "M.Tech", "M.Sc", "PhD"  ] ], Field(description="Highest qualification")] = None
    
    salary: Annotated[Optional[int],Field(ge=10000, le=1000000,description="Salary of the teacher")] = None

    min_salary: Annotated[Optional[int],Field(ge=10000, le=100000,description="Minimum salary of teacher")] = None

    max_salary: Annotated[Optional[int],Field(ge=10000, le=100000,description="Maximum salary of teacher")] = None

    experience: Annotated[Optional[int],Field(ge=0, le=50,description="Exact teaching experience in years")] = None

    min_experience: Annotated [Optional[int], Field( ge=0,le=50, description="Minimum teaching experience in years")] = None

    max_experience: Annotated[Optional[int], Field( ge=0,le=50, description="Maximum teaching experience in years")] = None

    date_of_joining: Optional[date] = None

    joined_after: Optional[date] = None

    joined_before: Optional[date] = None

    is_verified: Optional[bool] = None

    is_active: Optional[bool] = None

    # ---------------- Experience Filters ----------------

    min_experience: Annotated[ Optional[int],Field(ge=0, le=50, description="Minimum experience")] = None

    max_experience: Annotated[ Optional[int], Field(ge=0, le=50, description="Maximum experience")] = None

    # ---------------- Salary Filters ----------------

    min_salary: Annotated[ Optional[float], Field(ge=10000, description="Minimum salary") ] = None

    max_salary: Annotated[ Optional[float], Field(ge=10000, description="Maximum salary")] = None

    # ---------------- Sorting ----------------

    sort_by: Annotated[ Optional[ Literal[ "first_name", "last_name", "age", "experience", "salary", "department", "designation", "city", "date_of_joining" ] ], Field(description="Sort field")] = None

    sort_order: Annotated[ Optional[Literal["asc", "desc"]], Field(description="Sorting order")] = "asc"

    # ---------------- Pagination ----------------

    page: Annotated[ int, Field(ge=1, description="Page number") ] = 1

    limit: Annotated[ int, Field(ge=1, le=100, description="Records per page")] = 10


class TeacherResponse(Teacher):

    @computed_field
    @property
    def full_name(self) -> str:

        if self.qualification == "PhD":
            return f"Dr. {self.first_name} {self.last_name}"

        return f"Prof. {self.first_name} {self.last_name}"

      
    


