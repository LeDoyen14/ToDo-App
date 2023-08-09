from fastapi import FastAPI

from app.api.api_v1.router import router
from app.core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.models.user_model import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)


@app.on_event("startup")
async def app_init():
    # Initialize application services
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).todo
    await init_beanie(
        database=db_client,
        document_models=[
            User
        ]
    )

app.include_router(router, prefix=settings.API_V1_STR)
