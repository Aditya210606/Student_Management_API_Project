from sqlalchemy import String, Integer, Time, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from datetime import datetime, time

from database.database import Base


class TimetableModel(Base):

    __tablename__ = "timetable"

    timetable_id: Mapped[str] = mapped_column(String(10), primary_key=True, index=True)

    department_id: Mapped[str] = mapped_column( ForeignKey("departments.department_id"), nullable=False)

    semester: Mapped[int] = mapped_column(Integer, nullable=False)

    section: Mapped[str] = mapped_column(String(5), nullable=False)

    subject_id: Mapped[str] = mapped_column(ForeignKey("subjects.subject_id"), nullable=False)

    teacher_id: Mapped[str] = mapped_column(ForeignKey("teachers.teacher_id"), nullable=False)

    day: Mapped[str] = mapped_column(String(15), nullable=False)

    lecture_number: Mapped[int] = mapped_column(Integer, nullable=False)

    start_time: Mapped[time] = mapped_column(Time, nullable=False)

    end_time: Mapped[time] = mapped_column(Time, nullable=False)

    classroom: Mapped[str] = mapped_column(String(20), nullable=False)

    academic_year: Mapped[str] = mapped_column(String(20), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    created_at: Mapped[datetime] = mapped_column( DateTime,default=datetime.utcnow, nullable=False )

    updated_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False )


    department = relationship("DepartmentModel",back_populates="timetables")

    subject = relationship("SubjectModel",back_populates="timetables")

    teacher = relationship( "TeacherModel", back_populates="timetables")