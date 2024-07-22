from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
import uvicorn

from api import router as api_router 
from core.config import settings
from core.models import db_helper

@asynccontextmanager
async def lifespan(app: FastAPI):
    #startup
    yield
    #shutdown
    db_helper.dispose()

main_app = FastAPI(
    lifespan=lifespan,
    default_response_class=ORJSONResponse
)
main_app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app", 
        reload=True,
        host=settings.run.host,
        port=settings.run.port
    )