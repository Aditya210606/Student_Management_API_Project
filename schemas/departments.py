from pydantic import BaseModel, Field, EmailStr
from typing import Annotated,Optional,Literal
from datetime import date

 
class Department(BaseModel):
 
 
 department_id: Annotated[str, Field(..., description="Department ID", examples=["D001"])]

 department_name: Annotated[str, Field(..., min_length=3, max_length=100, description="Department name")]

 department_code: Annotated[str, Field(..., min_length=2, max_length=10, description="Department code", examples=["AIDS", "CSE"])]

 hod_id: Annotated[str, Field(..., description="HOD ID", examples=["T001"])]

 hod_name: Annotated[str, Field(..., description="HOD name")]

 building: Annotated[str, Field(..., min_length=2, max_length=50, description="Building name")]

 floor: Annotated[int, Field(..., ge=0, le=20, description="Floor number")]

 office_room: Annotated[str, Field(..., description="Department office room", examples=["301"])]

 office_email: Annotated[EmailStr, Field(..., description="Official department email")]

 office_phone: Annotated[str, Field(..., min_length=10, max_length=10, description="Office contact number", examples=["9876543210"])]

 description: Annotated[str, Field(..., min_length=5, max_length=500, description="Department description")]

 established_year: Annotated[int, Field(..., ge=1950, le=2100, description="Department establishment year")]

 is_active: Annotated[bool, Field(default=True, description="Department active status")]


class UpdateDepartment(BaseModel):

 department_id: Optional[Annotated[str, Field(description="Department ID", examples=["D001"])]] = None
 department_name: Optional[Annotated[str, Field(min_length=3, max_length=100, description="Department name")]] = None
 department_code: Optional[Annotated[str, Field(min_length=2, max_length=10, description="Department code", examples=["AIDS", "CSE"])]] = None
 hod_id: Optional[Annotated[str, Field(description="HOD ID", examples=["T001"])]] = None
 hod_name: Optional[Annotated[str, Field(description="HOD Name ID")]] = None
 building: Optional[Annotated[str, Field(min_length=2, max_length=50, description="Building name")]] = None
 floor: Optional[Annotated[int, Field(ge=0, le=20, description="Floor number")]] = None
 office_room: Optional[Annotated[str, Field(description="Department office room", examples=["301"])]] = None
 office_email: Optional[Annotated[EmailStr, Field(description="Official department email")]] = None
 office_phone: Optional[Annotated[str, Field(min_length=10, max_length=10, description="Office contact number", examples=["9876543210"])]] = None
 description: Optional[Annotated[str, Field(min_length=5, max_length=500, description="Department description")]] = None
 established_year: Optional[Annotated[int, Field(ge=1950, le=2100, description="Department establishment year")]] = None
 is_active: Optional[Annotated[bool, Field(description="Department active status")]] = None

class SearchDepartment(BaseModel):
 
    department_id: Annotated[Optional[str], Field(description="Department ID")] = None

    department_name: Annotated[Optional[str], Field(description="Department name")] = None

    department_code: Annotated[Optional[str], Field(description="Department code")] = None

    hod_id: Annotated[Optional[str], Field(description="HOD Teacher ID")] = None

    hod_name: Annotated[Optional[str], Field(description="HOD name")] = None

    building: Annotated[Optional[str], Field(description="Building name")] = None

    floor: Annotated[Optional[int], Field(ge=0, le=20, description="Floor number")] = None

    office_email: Annotated[Optional[EmailStr], Field(description="Department email")] = None

    office_phone: Annotated[Optional[str], Field(min_length=10, max_length=10, description="Department Phone no.")] = None

    established_year: Annotated[Optional[int], Field(ge=1950, le=2100, description="Established year")] = None

    is_active: Annotated[Optional[bool], Field(description="Department status")] = None

    created_at: Annotated[Optional[bool], Field(description="Department created at ")] = None
    # Sorting
    sort_by: Annotated[ Optional[ Literal[  "department_name", "hod_name", "building", "floor", "created_at","is_active" ] ], Field(description="Sort field")] = None

    sort_order: Annotated[ Optional[Literal["asc", "desc"]], Field(description="Sort order")] = "asc"

    # Pagination
    page: Annotated[ Optional[int],  Field(ge=1, description="Page number") ] = 1

    limit: Annotated[ Optional[int], Field(ge=1, le=100, description="Records per page")] = 10


class DepartmentResponse(Department):

    department_id: str
    department_name: str
    department_code: str
    hod_id: str
    hod_name: str
    building: str
    floor: int
    office_room: str
    office_email: EmailStr
    office_phone: str
    description: str
    established_year: int
    is_active: bool

    model_config = {
        "from_attributes": True
    }