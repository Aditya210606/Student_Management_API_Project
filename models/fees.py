from sqlalchemy import String, Integer, Float, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, date

from database.database import Base


class FeesModel(Base):

    __tablename__ = "fees"

    fee_id: Mapped[str] = mapped_column(String(10), primary_key=True, index=True)

    student_id: Mapped[str] = mapped_column(String(10), nullable=False)

    academic_year: Mapped[str] = mapped_column(String(20), nullable=False)

    semester: Mapped[int] = mapped_column(Integer, nullable=False)

    tuition_fee: Mapped[float] = mapped_column(Float, nullable=False)

    library_fee: Mapped[float] = mapped_column(Float, default=0, nullable=False)

    exam_fee: Mapped[float] = mapped_column(Float, default=0, nullable=False)

    hostel_fee: Mapped[float] = mapped_column(Float, default=0, nullable=False)

    transport_fee: Mapped[float] = mapped_column(Float, default=0, nullable=False)

    other_fee: Mapped[float] = mapped_column(Float, default=0, nullable=False)

    total_fee: Mapped[float] = mapped_column(Float, nullable=False)

    paid_amount: Mapped[float] = mapped_column(Float, nullable=False)

    pending_amount: Mapped[float] = mapped_column(Float, nullable=False)

    payment_status: Mapped[str] = mapped_column(String(20), nullable=False)

    payment_method: Mapped[str] = mapped_column(String(20), nullable=False)

    payment_date: Mapped[date] = mapped_column(Date, nullable=True)

    transaction_id: Mapped[str] = mapped_column(String(100), nullable=True)

    remarks: Mapped[str] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, nullable=False)

    updated_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False )