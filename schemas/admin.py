from pydantic import BaseModel, Field
from typing import Annotated, Literal,Optional
from datetime import date


class Admin(BaseModel):

    admin_id: Annotated[str, Field(..., description="Admin ID", examples=["A001"])]

    first_name: Annotated[str, Field(..., min_length=2, max_length=30, description="First Name")]

    last_name: Annotated[str, Field(..., min_length=2, max_length=30, description="Last Name")]

    email: Annotated[str, Field(..., description="Email Address", examples=["admin@college.edu"])]

    phone_number: Annotated[str, Field(..., min_length=10, max_length=10, description="Phone Number")]

    password: Annotated[str, Field(..., min_length=8, max_length=255, description="Password")]

    role: Annotated[ Literal["Super Admin", "Admin", "Academic Admin", "Accounts Admin"], Field(..., description="Admin Role")]

    date_of_joining: Annotated[ date, Field(..., description="Date of Joining")]

    is_active: Annotated[ bool, Field(default=True, description="Active Status")]

    profile_image: Annotated[ str, Field(default="default_admin.png", description="Profile Image") ]

class UpdateAdmin(BaseModel):

    admin_id: Annotated[Optional[str], Field(description="Admin ID", examples=["A001"])] = None

    first_name: Annotated[Optional[str], Field(min_length=2, max_length=30, description="First Name")] = None

    last_name: Annotated[Optional[str], Field(min_length=2, max_length=30, description="Last Name")] = None

    email: Annotated[Optional[str], Field(description="Email Address", examples=["admin@college.edu"])] = None

    phone_number: Annotated[Optional[str], Field(min_length=10, max_length=10, description="Phone Number")] = None

    password: Annotated[Optional[str], Field(min_length=8, max_length=255, description="Password")] = None

    role: Annotated[ Optional[Literal["Super Admin", "Admin", "Academic Admin", "Accounts Admin"]], Field(description="Admin Role")] = None

    date_of_joining: Annotated[ Optional[date],  Field(description="Date of Joining")] = None

    is_active: Annotated[ Optional[bool], Field(description="Active Status")] = None

    profile_image: Annotated[ Optional[str], Field(description="Profile Image")] = None


class SearchAdmin(BaseModel):

    admin_id: Annotated[Optional[str], Field(description="Admin ID")] = None

    first_name: Annotated[Optional[str], Field(description="First Name")] = None

    last_name: Annotated[Optional[str], Field(description="Last Name")] = None

    email: Annotated[Optional[str], Field(description="Email Address")] = None

    phone_number: Annotated[Optional[str], Field(description="Phone Number")] = None

    role: Annotated[ Optional[Literal["Super Admin", "Admin", "Academic Admin", "Accounts Admin"]], Field(description="Admin Role")] = None

    date_of_joining: Annotated[ Optional[date], Field(description="Date of Joining") ] = None

    is_active: Annotated[ Optional[bool], Field(description="Active Status") ] = None

    sort_by: Annotated[
        Optional[
            Literal[
                "admin_id",
                "first_name",
                "last_name",
                "email",
                "phone_number",
                "role",
                "date_of_joining",
                "is_active",
                "created_at",
                "updated_at"
            ]
        ], Field(description="Sort By")] = None

    sort_order: Annotated[ Optional[Literal["asc", "desc"]], Field(description="Sort Order") ] = "asc"

    page: Annotated[ Optional[int], Field(ge=1, description="Page Number") ] = 1

    limit: Annotated[  Optional[int], Field(ge=1, le=100, description="Records Per Page")] = 10


class AdminResponse(BaseModel):

    admin_id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str
    password: str
    role: Literal["Super Admin", "Admin", "Academic Admin", "Accounts Admin"]
    date_of_joining: date
    is_active: bool
    profile_image: str

    model_config = {
        "from_attributes": True
    }

