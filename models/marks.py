from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from database.base import Base


class MarksModel(Base):

    __tablename__ = "marks"

    mark_id: Mapped[str] = mapped_column(String(10), primary_key=True, index=True)

    student_id: Mapped[str] = mapped_column(String(10), nullable=False)

    subject_id: Mapped[str] = mapped_column(String(10), nullable=False)

    teacher_id: Mapped[str] = mapped_column(String(10), nullable=False)

    internal_marks: Mapped[float] = mapped_column(Float, nullable=False)

    external_marks: Mapped[float] = mapped_column(Float, nullable=False)

    practical_marks: Mapped[float] = mapped_column(Float, default=0, nullable=False)

    total_marks: Mapped[float] = mapped_column(Float, nullable=False)

    grade: Mapped[str] = mapped_column(String(5), nullable=False)

    result: Mapped[str] = mapped_column(String(10), nullable=False)

    remarks: Mapped[str] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, nullable=False)

    updated_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False )