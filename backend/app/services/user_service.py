from typing import Optional

from app.schemas.user_schema import UserAuth, UserOut
from app.models.user_model import User
from app.core.security import get_password, verify_password


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
            user_name=user.username,
            email=user.email,
            hashed_password=get_password(user.password)
        )
        await user_in.insert()

        user_out = UserOut(
            user_id=user_in.user_id,
            username=user_in.user_name,
            email=user_in.email,
            first_name=user_in.first_name,
            last_name=user_in.last_name,
            disabled=False
        )
        return user_out

    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        user = await UserService.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(password=password, hashed_password=user.hashed_password):
            return None
        return user

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        user = await User.find_one(User.email == email)
        return user

    @staticmethod
    async def get_user_by_id(user_id: str) -> Optional[User]:
        user = await User.find_one(User.user_id == user_id)
        return user
