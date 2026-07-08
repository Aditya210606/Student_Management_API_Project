from pydantic import BaseModel, Field
from typing import Annotated, Literal,Optional
from datetime import time


class Timetable(BaseModel):

    timetable_id: Annotated[str, Field(..., description="Timetable ID", examples=["TT001"])]

    department_id: Annotated[str, Field(...,description="department id", examples=['D001'])]

    semester: Annotated[int, Field(..., ge=1, le=8, description="Semester")]

    section: Annotated[Literal["A", "B", "C"], Field(..., description="Section")]

    subject_id: Annotated[str, Field(..., description="Subject ID", examples=["SUB001"])]

    teacher_id: Annotated[str, Field(..., description="Teacher ID", examples=["T001"])]

    day: Annotated[Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], Field(..., description="Day")]

    lecture_number: Annotated[int, Field(..., ge=1, le=8, description="Lecture Number")]

    start_time: Annotated[time, Field(..., description="Start Time")]

    end_time: Annotated[time, Field(..., description="End Time")]

    classroom: Annotated[str, Field(..., max_length=20, description="Classroom", examples=["CR301"])]

    academic_year: Annotated[str, Field(..., description="Academic Year", examples=["2026-2027"])]

    is_active: Annotated[bool, Field(default=True, description="Timetable Status")]


class UpdateTimetable(BaseModel):

    timetable_id: Annotated[Optional[str], Field(description="Timetable ID", examples=["TT001"])] = None

    department_id: Annotated[Optional[str], Field(description="department_id")] = None

    semester: Annotated[Optional[int], Field(ge=1, le=8, description="Semester")] = None

    section: Annotated[Optional[Literal["A", "B", "C"]], Field(description="Section")] = None

    subject_id: Annotated[Optional[str], Field(description="Subject ID", examples=["SUB001"])] = None

    teacher_id: Annotated[Optional[str], Field(description="Teacher ID", examples=["T001"])] = None

    day: Annotated[Optional[Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]], Field(description="Day")] = None

    lecture_number: Annotated[Optional[int], Field(ge=1, le=8, description="Lecture Number")] = None

    start_time: Annotated[Optional[time], Field(description="Start Time")] = None

    end_time: Annotated[Optional[time], Field(description="End Time")] = None

    classroom: Annotated[Optional[str], Field(max_length=20, description="Classroom")] = None

    academic_year: Annotated[Optional[str], Field(description="Academic Year", examples=["2026-2027"])] = None

    is_active: Annotated[Optional[bool], Field(description="Timetable Status")] = None



class SearchTimetable(BaseModel):

    timetable_id: Annotated[Optional[str], Field(description="Timetable ID")] = None

    department_id: Annotated[Optional[str], Field(description="department_id")] = None

    semester: Annotated[Optional[int], Field(ge=1, le=8, description="Semester")] = None

    section: Annotated[Optional[Literal["A", "B", "C"]], Field(description="Section")] = None

    subject_id: Annotated[Optional[str], Field(description="Subject ID")] = None

    teacher_id: Annotated[Optional[str], Field(description="Teacher ID")] = None

    day: Annotated[Optional[Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]], Field(description="Day")] = None

    lecture_number: Annotated[Optional[int], Field(ge=1, le=8, description="Lecture Number")] = None

    start_time: Annotated[Optional[time], Field(description="Start Time")] = None

    end_time: Annotated[Optional[time], Field(description="End Time")] = None

    classroom: Annotated[Optional[str], Field(description="Classroom")] = None

    academic_year: Annotated[Optional[str], Field(description="Academic Year")] = None

    is_active: Annotated[Optional[bool], Field(description="Timetable Status")] = None

    sort_by: Annotated[
        Optional[
            Literal[
                "timetable_id",
                "department",
                "semester",
                "section",
                "subject_id",
                "teacher_id",
                "day",
                "lecture_number",
                "start_time",
                "end_time",
                "classroom",
                "academic_year",
                "is_active"
            ]
        ], Field(description="Sort By")] = None

    sort_order: Annotated[ Optional[Literal["asc", "desc"]], Field(description="Sort Order")] = "asc"

    page: Annotated[ Optional[int], Field(ge=1, description="Page Number")] = 1

    limit: Annotated[ Optional[int], Field(ge=1, le=100, description="Records Per Page")] = 10


from pydantic import BaseModel
from typing import Literal
from datetime import time


class TimetableResponse(BaseModel):

    timetable_id: str
    department_id: str
    semester: int
    section: Literal["A", "B", "C"]
    subject_id: str
    teacher_id: str
    day: Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    lecture_number: int
    start_time: time
    end_time: time
    classroom: str
    academic_year: str
    is_active: bool

    model_config = {
        "from_attributes": True
    }    




