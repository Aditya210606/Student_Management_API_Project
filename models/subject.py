from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean

from database.base import Base


class SubjectModel(Base):

    __tablename__ = "subjects"

    subject_id: Mapped[str] = mapped_column(String(10), primary_key=True, index=True)

    subject_name: Mapped[str] = mapped_column(String(100), nullable=False)

    subject_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)

    department: Mapped[str] = mapped_column(String(50), nullable=False)

    semester: Mapped[int] = mapped_column(Integer, nullable=False)

    credits: Mapped[int] = mapped_column(Integer, nullable=False)

    subject_type: Mapped[str] = mapped_column(String(30), nullable=False)

    teacher_id: Mapped[str] = mapped_column(String(10), nullable=False)

    description: Mapped[str] = mapped_column(String(500), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)