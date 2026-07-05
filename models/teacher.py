from datetime import date, datetime
from sqlalchemy import String, Integer, Float, Boolean, Date, DateTime,ForeignKey
from sqlalchemy.orm import Mapped, mapped_column,relationship
from database.base import Base


class TeacherModel(Base):

    __tablename__ = "teachers"

    teacher_id: Mapped[str] = mapped_column( String(10), primary_key=True, index=True )

    first_name: Mapped[str] = mapped_column( String(30), nullable=False)

    last_name: Mapped[str] = mapped_column( String(30), nullable=False)

    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

    phone_number: Mapped[str] = mapped_column( String(10), unique=True, nullable=False)

    password_hash: Mapped[str] = mapped_column( String(255), nullable=False )

    age: Mapped[int] = mapped_column( Integer, nullable=False)

    gender: Mapped[str] = mapped_column( String(10), nullable=False )

    date_of_birth: Mapped[date] = mapped_column( Date, nullable=False )

    city: Mapped[str] = mapped_column( String(50), nullable=False)

    address: Mapped[str] = mapped_column( String(255), nullable=False)

    department_id: Mapped[str] = mapped_column( ForeignKey("departments.department_id"), nullable=False )

    designation: Mapped[str] = mapped_column( String(50), nullable=False)

    qualification: Mapped[str] = mapped_column( String(20), nullable=False)

    experience: Mapped[int] = mapped_column( Integer, nullable=False)

    salary: Mapped[float] = mapped_column( Float, nullable=False)

    date_of_joining: Mapped[date] = mapped_column( Date, nullable=False )

    is_verified: Mapped[bool] = mapped_column( Boolean, default=False, nullable=False )

    is_active: Mapped[bool] = mapped_column( Boolean, default=True, nullable=False)

    profile_image: Mapped[str] = mapped_column( String(255), default="default_teacher.png", nullable=False )

    created_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, nullable=False )

    updated_at: Mapped[datetime] = mapped_column( DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)    


    #relationship
    department = relationship("DepartmentModel",back_populates="teachers")
    subjects = relationship("SubjectModel",back_populates="teacher")
    marks = relationship(
    "MarksModel",
    back_populates="teacher"
)
    
    timetables = relationship(
    "TimetableModel",
    back_populates="teacher"
)