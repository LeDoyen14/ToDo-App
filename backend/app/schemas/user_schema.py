from uuid import UUID
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.models.user_model import User


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., description="user name")
    password: str = Field(..., description="user password")


class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    disabled: bool = False
