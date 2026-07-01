from pydantic import BaseModel, Field
from typing import Annotated, Literal, Optional


class Marks(BaseModel):

    mark_id: Annotated[str, Field(..., description="Marks ID", examples=["M001"])]

    student_id: Annotated[str, Field(..., description="Student ID", examples=["S001"])]

    subject_id: Annotated[str, Field(..., description="Subject ID", examples=["SUB001"])]

    teacher_id: Annotated[str, Field(..., description="Teacher ID", examples=["T001"])]

    internal_marks: Annotated[float, Field(..., ge=0, le=30, description="Internal Marks")]

    external_marks: Annotated[float, Field(..., ge=0, le=70, description="External Marks")]

    practical_marks: Annotated[Optional[float], Field(default=0, ge=0, le=50, description="Practical Marks")] = 0

    total_marks: Annotated[float, Field(..., ge=0, le=150, description="Total Marks")]

    grade: Annotated[ Literal["O", "A+", "A", "B+", "B", "C", "F"], Field(..., description="Grade")]

    result: Annotated[ Literal["Pass", "Fail"], Field(..., description="Result") ]

    remarks: Annotated[ Optional[str],  Field(default=None, max_length=255, description="Remarks")] = None




class UpdateMarks(BaseModel):

    mark_id: Annotated[Optional[str], Field(description="Marks ID", examples=["M001"])] = None

    student_id: Annotated[Optional[str], Field(description="Student ID", examples=["S001"])] = None

    subject_id: Annotated[Optional[str], Field(description="Subject ID", examples=["SUB001"])] = None

    teacher_id: Annotated[Optional[str], Field(description="Teacher ID", examples=["T001"])] = None

    internal_marks: Annotated[Optional[float], Field(ge=0, le=30, description="Internal Marks")] = None

    external_marks: Annotated[Optional[float], Field(ge=0, le=70, description="External Marks")] = None

    practical_marks: Annotated[Optional[float], Field(ge=0, le=50, description="Practical Marks")] = None

    total_marks: Annotated[Optional[float], Field(ge=0, le=150, description="Total Marks")] = None

    grade: Annotated[ Optional[Literal["O", "A+", "A", "B+", "B", "C", "F"]],Field(description="Grade")] = None

    result: Annotated[ Optional[Literal["Pass", "Fail"]], Field(description="Result") ] = None

    remarks: Annotated[ Optional[str], Field(max_length=255, description="Remarks")] = None  


class SearchMarks(BaseModel):

    mark_id: Annotated[Optional[str], Field(description="Marks ID")] = None
    student_id: Annotated[Optional[str], Field(description="Student ID")] = None
    subject_id: Annotated[Optional[str], Field(description="Subject ID")] = None
    teacher_id: Annotated[Optional[str], Field(description="Teacher ID")] = None
    internal_marks: Annotated[Optional[float], Field(ge=0, le=30, description="Internal Marks")] = None
    external_marks: Annotated[Optional[float], Field(ge=0, le=70, description="External Marks")] = None
    practical_marks: Annotated[Optional[float], Field(ge=0, le=50, description="Practical Marks")] = None
    total_marks: Annotated[Optional[float], Field(ge=0, le=150, description="Total Marks")] = None
    grade: Annotated[Optional[Literal["O", "A+", "A", "B+", "B", "C", "F"]], Field(description="Grade")] = None
    result: Annotated[Optional[Literal["Pass", "Fail"]], Field(description="Result")] = None

    sort_by: Annotated[Optional[Literal[ "mark_id", "student_id", "subject_id", "teacher_id", "internal_marks", "external_marks", "practical_marks", "total_marks", "grade", "result"]], Field(description="Sort By")] = None

    sort_order: Annotated[Optional[Literal["asc", "desc"]], Field(description="Sort Order")] = "asc"

    page: Annotated[Optional[int], Field(ge=1, description="Page Number")] = 1

    limit: Annotated[Optional[int], Field(ge=1, le=100, description="Records Per Page")] = 10


class MarksResponse(BaseModel):

    mark_id: str
    student_id: str
    subject_id: str
    teacher_id: str
    internal_marks: float
    external_marks: float
    practical_marks: Optional[float] = 0
    total_marks: float
    grade: Literal["O", "A+", "A", "B+", "B", "C", "F"]
    result: Literal["Pass", "Fail"]
    remarks: Optional[str] = None

    model_config = {
        "from_attributes": True
    }