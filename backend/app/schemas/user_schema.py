from uuid import UUID
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., description="user name")
    password: str = Field(..., description="user password")


class UserOut(BaseModel):
    user_id: UUID = Field(..., description="user id")
    username: str = Field(..., description="user name")
    email: EmailStr = Field(..., description="user email")
    firstname: Optional[str] = Field(..., description="first name")
    lastname: Optional[str] = Field(..., description="last name")
    disabled: bool = False
