from datetime import date, datetime
from sqlalchemy import String,Integer,Float,Boolean,Date,DateTime,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database.base import Base



class Student(Base):
    __tablename__ = "students"
       
    student_id: Mapped[str] = mapped_column(String(10), primary_key=True)
    first_name: Mapped[str] = mapped_column( String(30),nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True,nullable=False)
    phone_number: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column( String(255), nullable=False)
    age: Mapped[int] = mapped_column( Integer, nullable=False)
    gender: Mapped[str] = mapped_column( String(10), nullable=False)
    date_of_birth: Mapped[date] = mapped_column( Date, nullable=False)
    city: Mapped[str] = mapped_column( String(50),nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    year: Mapped[int] = mapped_column( Integer, nullable=False)
    department_id: Mapped[str] = mapped_column(ForeignKey("departments.department_id") , nullable=False)
    semester: Mapped[int] = mapped_column( Integer,nullable=False)
    admission_year: Mapped[int] = mapped_column( Integer, nullable=False)
    cgpa: Mapped[float] = mapped_column( Float, default=0.0)
    attendance_percentage: Mapped[float] = mapped_column( Float, default=0.0,nullable=False)
    profile_image: Mapped[str] = mapped_column( String(255), nullable=False, default="default.png")
    is_verified: Mapped[bool] = mapped_column( Boolean, default=False)
    is_active: Mapped[bool] = mapped_column( Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow,)
    updated_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, onupdate=datetime.utcnow,)


     #relationship
    department = relationship('DepartmentModel',back_populates="students")