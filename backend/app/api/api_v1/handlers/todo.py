from fastapi import APIRouter


todo_router = APIRouter()

@todo_router.get('/', summary="Get all todo of the user", response_model=None)
