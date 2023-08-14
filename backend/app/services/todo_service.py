from datetime import datetime
from typing import List

from app.models.todo_model import Todo
from app.models.user_model import User
from app.schemas.todo_schema import TodoCreate


class TodoService:
    @staticmethod
    async def list_todos(user: User) -> List[Todo]:
        todos = await Todo.find(Todo.owner.id == user.user_id).to_list()
        return todos

    @staticmethod
    async def create_todo(data: TodoCreate, user: User) -> Todo:
        todo = Todo(**data.dict(), owner=user, created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        return await todo.create()
