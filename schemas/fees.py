from pydantic import BaseModel, Field
from typing import Annotated, Optional, Literal
from datetime import date


class Fees(BaseModel):

    fee_id: Annotated[str, Field(..., description="Fee ID", examples=["F001"])]

    student_id: Annotated[str, Field(..., description="Student ID", examples=["S001"])]

    academic_year: Annotated[str, Field(..., description="Academic Year", examples=["2026-2027"])]

    semester: Annotated[int, Field(..., ge=1, le=8, description="Semester")]

    tuition_fee: Annotated[float, Field(..., ge=0, description="Tuition Fee")]

    library_fee: Annotated[float, Field(default=0, ge=0, description="Library Fee")] = 0

    exam_fee: Annotated[float, Field(default=0, ge=0, description="Exam Fee")] = 0

    hostel_fee: Annotated[float, Field(default=0, ge=0, description="Hostel Fee")] = 0

    transport_fee: Annotated[float, Field(default=0, ge=0, description="Transport Fee")] = 0

    other_fee: Annotated[float, Field(default=0, ge=0, description="Other Fee")] = 0

    total_fee: Annotated[float, Field(..., ge=0, description="Total Fee")]

    paid_amount: Annotated[float, Field(..., ge=0, description="Paid Amount")]

    pending_amount: Annotated[float, Field(..., ge=0, description="Pending Amount")]

    payment_status: Annotated[ Literal["Paid", "Partial", "Pending"], Field(..., description="Payment Status")]

    payment_method: Annotated[ Literal["Cash", "UPI", "Card", "Net Banking"], Field(..., description="Payment Method")]

    payment_date: Annotated[ Optional[date], Field(default=None, description="Payment Date")] = None

    transaction_id: Annotated[ Optional[str], Field(default=None, description="Transaction ID", examples=["TXN123456"])] = None

    remarks: Annotated[ Optional[str], Field(default=None, max_length=255, description="Remarks") ] = None


from pydantic import BaseModel, Field
from typing import Annotated, Optional, Literal
from datetime import date


class UpdateFees(BaseModel):

    fee_id: Annotated[Optional[str], Field(description="Fee ID", examples=["F001"])] = None

    student_id: Annotated[Optional[str], Field(description="Student ID", examples=["S001"])] = None

    academic_year: Annotated[Optional[str], Field(description="Academic Year", examples=["2026-2027"])] = None

    semester: Annotated[Optional[int], Field(ge=1, le=8, description="Semester")] = None

    tuition_fee: Annotated[Optional[float], Field(ge=0, description="Tuition Fee")] = None

    library_fee: Annotated[Optional[float], Field(ge=0, description="Library Fee")] = None

    exam_fee: Annotated[Optional[float], Field(ge=0, description="Exam Fee")] = None

    hostel_fee: Annotated[Optional[float], Field(ge=0, description="Hostel Fee")] = None

    transport_fee: Annotated[Optional[float], Field(ge=0, description="Transport Fee")] = None

    other_fee: Annotated[Optional[float], Field(ge=0, description="Other Fee")] = None

    total_fee: Annotated[Optional[float], Field(ge=0, description="Total Fee")] = None

    paid_amount: Annotated[Optional[float], Field(ge=0, description="Paid Amount")] = None

    pending_amount: Annotated[Optional[float], Field(ge=0, description="Pending Amount")] = None

    payment_status: Annotated[ Optional[Literal["Paid", "Partial", "Pending"]], Field(description="Payment Status") ] = None

    payment_method: Annotated[ Optional[Literal["Cash", "UPI", "Card", "Net Banking"]], Field(description="Payment Method") ] = None

    payment_date: Annotated[ Optional[date], Field(description="Payment Date") ] = None

    transaction_id: Annotated[ Optional[str], Field(description="Transaction ID", examples=["TXN123456"]) ] = None

    remarks: Annotated[ Optional[str], Field(max_length=255, description="Remarks") ] = None    



class SearchFees(BaseModel):

    fee_id: Annotated[Optional[str], Field(description="Fee ID")] = None
    student_id: Annotated[Optional[str], Field(description="Student ID")] = None
    academic_year: Annotated[Optional[str], Field(description="Academic Year")] = None
    semester: Annotated[Optional[int], Field(ge=1, le=8, description="Semester")] = None
    tuition_fee: Annotated[Optional[float], Field(ge=0, description="Tuition Fee")] = None
    library_fee: Annotated[Optional[float], Field(ge=0, description="Library Fee")] = None
    exam_fee: Annotated[Optional[float], Field(ge=0, description="Exam Fee")] = None
    hostel_fee: Annotated[Optional[float], Field(ge=0, description="Hostel Fee")] = None
    transport_fee: Annotated[Optional[float], Field(ge=0, description="Transport Fee")] = None
    other_fee: Annotated[Optional[float], Field(ge=0, description="Other Fee")] = None
    total_fee: Annotated[Optional[float], Field(ge=0, description="Total Fee")] = None
    paid_amount: Annotated[Optional[float], Field(ge=0, description="Paid Amount")] = None
    pending_amount: Annotated[Optional[float], Field(ge=0, description="Pending Amount")] = None
    payment_status: Annotated[Optional[Literal["Paid", "Partial", "Pending"]], Field(description="Payment Status")] = None
    payment_method: Annotated[Optional[Literal["Cash", "UPI", "Card", "Net Banking"]], Field(description="Payment Method")] = None
    payment_date: Annotated[Optional[date], Field(description="Payment Date")] = None
    transaction_id: Annotated[Optional[str], Field(description="Transaction ID")] = None

    sort_by: Annotated[
        Optional[
            Literal[
                "fee_id",
                "student_id",
                "academic_year",
                "semester",
                "tuition_fee",
                "library_fee",
                "exam_fee",
                "hostel_fee",
                "transport_fee",
                "other_fee",
                "total_fee",
                "paid_amount",
                "pending_amount",
                "payment_status",
                "payment_method",
                "payment_date",
                "transaction_id"
            ]
        ],
        Field(description="Sort By")
    ] = None

    sort_order: Annotated[Optional[Literal["asc", "desc"]], Field(description="Sort Order")] = "asc"

    page: Annotated[Optional[int], Field(ge=1, description="Page Number")] = 1

    limit: Annotated[Optional[int], Field(ge=1, le=100, description="Records Per Page")] = 10


from pydantic import BaseModel
from typing import Optional, Literal
from datetime import date


class FeesResponse(BaseModel):

    fee_id: str
    student_id: str
    academic_year: str
    semester: int
    tuition_fee: float
    library_fee: float
    exam_fee: float
    hostel_fee: float
    transport_fee: float
    other_fee: float
    total_fee: float
    paid_amount: float
    pending_amount: float
    payment_status: Literal["Paid", "Partial", "Pending"]
    payment_method: Literal["Cash", "UPI", "Card", "Net Banking"]
    payment_date: Optional[date] = None
    transaction_id: Optional[str] = None
    remarks: Optional[str] = None

    model_config = {
        "from_attributes": True
    }    
