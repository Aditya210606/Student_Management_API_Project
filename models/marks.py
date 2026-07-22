from sqlalchemy import String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from datetime import datetime
from database.base import Base


class MarksModel(Base):

    __tablename__ = "marks"

    mark_id: Mapped[str] = mapped_column(String(10), primary_key=True, index=True)

    student_id: Mapped[str] = mapped_column( ForeignKey("students.student_id"), nullable=False)

    subject_id: Mapped[str] = mapped_column( ForeignKey("subjects.subject_id"), nullable=False)

    teacher_id: Mapped[str] = mapped_column( ForeignKey("teachers.teacher_id"), nullable=False)

    internal_marks: Mapped[float] = mapped_column(Float, nullable=False)

    external_marks: Mapped[float] = mapped_column(Float, nullable=False)

    practical_marks: Mapped[float] = mapped_column(Float, default=0, nullable=False)

    total_marks: Mapped[float] = mapped_column(Float, nullable=False)

    grade: Mapped[str] = mapped_column(String(5), nullable=False)

    result: Mapped[str] = mapped_column(String(10), nullable=False)

    remarks: Mapped[str] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, nullable=False)

    updated_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False )

    students = relationship( "Student", back_populates="marks")

    subject = relationship("SubjectModel", back_populates="marks")

    teacher = relationship("TeacherModel",back_populates="marks")