from pydantic import BaseModel, Field
from typing import Annotated,Optional,Literal
from datetime import date


class Attendance(BaseModel):

   attendance_id: Annotated[ str,Field(..., examples=["AT001"])]

   student_id: Annotated[str,Field(..., examples=["S001"])]

   subject_id: Annotated[str,Field(..., examples=["SUB001"])]

   teacher_id: Annotated[ str,Field(..., examples=["T001"])]

   attendance_date: date

   lecture_number: Annotated[ int, Field(..., ge=1, le=8)]

   status: Annotated[Literal["Present", "Absent", "Late", "Leave"], Field(...)]

   remarks: Annotated[ Optional[str], Field(max_length=255)] = None


class UpdateAttendance(BaseModel):

    attendance_id: Annotated[ Optional[str], Field(description="Attendance ID", examples=["AT001"])] = None

    student_id: Annotated[ Optional[str], Field(description="Student ID", examples=["S001"])] = None

    subject_id: Annotated[ Optional[str], Field(description="Subject ID", examples=["SUB001"])] = None

    teacher_id: Annotated[ Optional[str], Field(description="Teacher ID", examples=["T001"])] = None

    attendance_date: Annotated[ Optional[date], Field(description="Attendance date")] = None

    lecture_number: Annotated[ Optional[int], Field(ge=1, le=8, description="Lecture number") ] = None

    status: Annotated[ Optional[Literal["Present", "Absent", "Late", "Leave"]],Field(description="Attendance status")] = None

    remarks: Annotated[ Optional[str], Field(max_length=255, description="Remarks")] = None



class SearchAttendance(BaseModel):

    attendance_id: Annotated[Optional[str], Field(description="Attendance ID")] = None
    student_id: Annotated[Optional[str], Field(description="Student ID")] = None
    subject_id: Annotated[Optional[str], Field(description="Subject ID")] = None
    teacher_id: Annotated[Optional[str], Field(description="Teacher ID")] = None
    attendance_date: Annotated[Optional[date], Field(description="Attendance Date")] = None
    lecture_number: Annotated[Optional[int], Field(ge=1, le=8, description="Lecture Number")] = None
    status: Annotated[Optional[Literal["Present", "Absent", "Late", "Leave"]], Field(description="Attendance Status")] = None
    sort_by: Annotated[Optional[Literal["attendance_id", "student_id", "subject_id", "teacher_id", "attendance_date", "lecture_number", "status"]], Field(description="Sort By")] = None
    sort_order: Annotated[Optional[Literal["asc", "desc"]], Field(description="Sort Order")] = "asc"
    page: Annotated[Optional[int], Field(ge=1, description="Page Number")] = 1
    limit: Annotated[Optional[int], Field(ge=1, le=100, description="Records Per Page")] = 10


class AttendanceResponse(Attendance):

    attendance_id: str
    student_id: str
    subject_id: str
    teacher_id: str
    attendance_date: date
    lecture_number: int
    status: Literal["Present", "Absent", "Late", "Leave"]
    remarks: Optional[str] = None

    model_config = {
    "from_attributes": True
}    