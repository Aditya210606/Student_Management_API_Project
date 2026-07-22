from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import String, Integer, Boolean, ForeignKey
from database.base import Base


class SubjectModel(Base):

    __tablename__ = "subjects"

    subject_id: Mapped[str] = mapped_column(  String(10),primary_key=True, index=True)

    subject_name: Mapped[str] = mapped_column(String(100), nullable=False)

    subject_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    department_id: Mapped[str] = mapped_column(ForeignKey("departments.department_id"), nullable=False)

    semester: Mapped[int] = mapped_column(Integer, nullable=False)

    credits: Mapped[int] = mapped_column(Integer, nullable=False)

    subject_type: Mapped[str] = mapped_column(String(30), nullable=False)

    teacher_id: Mapped[str] = mapped_column(ForeignKey("teachers.teacher_id"), nullable=False)

    description: Mapped[str] = mapped_column(String(500), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


    #relationship
    department = relationship("DepartmentModel", back_populates="subjects")
    teacher = relationship("TeacherModel", back_populates="subjects")
    marks = relationship("MarksModel",back_populates="subject")
    timetables = relationship(
    "TimetableModel",
    back_populates="subject"
)