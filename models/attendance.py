from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import String, Integer, Boolean,Date,DateTime,ForeignKey
from datetime import date,datetime
from database.base import Base

class AttendanceModel(Base):
 
 __tablename__ = "attendance"

 attendance_id: Mapped[str] = mapped_column(String(10), primary_key=True, index=True)

 student_id: Mapped[str] = mapped_column( ForeignKey("students.student_id"), nullable=False)

 subject_id: Mapped[str] = mapped_column(ForeignKey("subjects.subject_id"),nullable=False)

 teacher_id: Mapped[str] = mapped_column( ForeignKey("teachers.teacher_id"), nullable=False)

 attendance_date: Mapped[date] = mapped_column(Date, nullable=False)

 lecture_number: Mapped[int] = mapped_column(Integer, nullable=False)

 status: Mapped[str] = mapped_column(String(15), nullable=False)

 remarks: Mapped[str] = mapped_column(String(255), nullable=True)

 marked_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow,nullable=False)

 created_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, nullable=False)

 updated_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


 #relationship
 students = relationship( "Student", back_populates="attendance")

 