from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Boolean,Date,DateTime
from datetime import date,datetime

from database.base import Base


class DepartmentModel(Base):

    __tablename__ = "departments"

    department_id: Mapped[str] = mapped_column(String(10), primary_key=True, index=True)

    department_name: Mapped[str] = mapped_column(String(100), nullable=False)

    department_code: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)

    hod_id: Mapped[str] = mapped_column(String(10), nullable=False)

    hod_name: Mapped[str] = mapped_column(String(50), nullable=False)

    building: Mapped[str] = mapped_column(String(50), nullable=False)

    floor: Mapped[int] = mapped_column(Integer, nullable=False)

    office_room: Mapped[str] = mapped_column(String(20), nullable=False)

    office_email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    office_phone: Mapped[str] = mapped_column(String(10), nullable=False)

    description: Mapped[str] = mapped_column(String(500), nullable=False)

    established_year: Mapped[int] = mapped_column(Integer, nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, nullable=False )

    updated_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)