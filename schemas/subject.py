from typing import Annotated, Literal,Optional
from pydantic import BaseModel, Field

class Subject(BaseModel):

    subject_id: Annotated[str, Field(..., description="Subject ID", examples=["SUB001"])]

    subject_name: Annotated[str, Field(..., min_length=2, max_length=100, description="Subject name")]

    subject_code: Annotated[str, Field(..., min_length=2, max_length=20, description="Subject code", examples=["CS301"])]

    department: Annotated[ Literal["AI&DS", "CSE", "IT", "EXTC", "Mechanical", "Civil"], Field(..., description="Department offering the subject")]

    semester: Annotated[int, Field(..., ge=1, le=8, description="Semester")]

    credits: Annotated[int, Field(..., ge=1, le=6, description="Subject credits")]

    subject_type: Annotated[ Literal["Theory", "Practical", "Theory + Practical"], Field(..., description="Type of subject")]

    teacher_id: Annotated[str, Field(..., description="Teacher ID", examples=["T001"])]

    description: Annotated[str, Field(..., min_length=5, max_length=500, description="Subject description")]

    is_active: Annotated[bool, Field(default=True, description="Subject active status")]



class UpdateSubject(BaseModel):

    subject_id: Annotated[Optional[str], Field(description="Subject ID", examples=["SUB001"])] = None

    subject_name: Annotated[Optional[str], Field(min_length=2, max_length=100, description="Subject name")] = None

    subject_code: Annotated[Optional[str], Field(min_length=2, max_length=20, description="Subject code", examples=["CS301"])] = None

    department: Annotated[ Optional[Literal["AI&DS", "CSE", "IT", "EXTC", "Mechanical", "Civil"]], Field(description="Department offering the subject")] = None

    semester: Annotated[Optional[int], Field(ge=1, le=8, description="Semester")] = None

    credits: Annotated[Optional[int], Field(ge=1, le=6, description="Subject credits")] = None

    subject_type: Annotated[ Optional[Literal["Theory", "Practical", "Theory + Practical"]], Field(description="Type of subject")] = None

    teacher_id: Annotated[Optional[str], Field(description="Teacher ID", examples=["T001"])] = None

    description: Annotated[ Optional[str], Field(min_length=5, max_length=500, description="Subject description")] = None

    is_active: Annotated[ Optional[bool], Field(description="Subject active status") ] = None    



class SearchSubject(BaseModel):

    subject_id: Annotated[Optional[str], Field(description="Subject ID")] = None

    subject_name: Annotated[Optional[str], Field(description="Subject name")] = None

    subject_code: Annotated[Optional[str], Field(description="Subject code")] = None

    department: Annotated[Optional[Literal["AI&DS", "CSE", "IT", "EXTC", "Mechanical", "Civil"]], Field(description="Department") ] = None

    semester: Annotated[  Optional[int],  Field(ge=1, le=8, description="Semester") ] = None

    credits: Annotated[ Optional[int], Field(ge=1, le=6, description="Credits")] = None

    subject_type: Annotated[ Optional[Literal["Theory", "Practical", "Theory + Practical"]], Field(description="Subject type")] = None

    teacher_id: Annotated[ Optional[str], Field(description="Teacher ID") ] = None

    is_active: Annotated[ Optional[bool], Field(description="Subject active status")] = None

    # Sorting
    sort_by: Annotated[Optional[ Literal[ "subject_name","subject_code", "department", "semester", "credits" ] ], Field(description="Sort field")] = None

    sort_order: Annotated[ Optional[Literal["asc", "desc"]], Field(description="Sort order")] = "asc"

    # Pagination
    page: Annotated[ Optional[int], Field(ge=1, description="Page number")] = 1

    limit: Annotated[ Optional[int], Field(ge=1, le=100, description="Records per page")] = 10    