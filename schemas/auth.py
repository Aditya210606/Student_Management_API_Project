from pydantic import BaseModel, Field
from typing import Annotated


class StudentLogin(BaseModel):

    student_id: Annotated[ str,Field( min_length=1, max_length=10, examples=["S001"] ) ]

    password: Annotated[str, Field( min_length=8,max_length=100, examples=["Password@123"] ) ]