from fastapi import APIRouter, Depends

from app.api.deps.user_deps import get_current_user
from app.models.todo_model import Todo
from app.models.user_model import User
from app.schemas.todo_schema import TodoOut, TodoCreate
from app.services.todo_service import TodoService

todo_router = APIRouter()


@todo_router.get('/', summary="Get all todo of the user", response_model=TodoOut)
async def list_todos(current_user: User = Depends(get_current_user)):
    return await TodoService.list_todos(current_user)


@todo_router.post('/create', summary="Create Todo", response_model=Todo)
async def create_todo(data: TodoCreate, current_user: User = Depends(get_current_user)):
    return await TodoService.create_todo(data, current_user)
