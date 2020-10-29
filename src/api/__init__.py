from fastapi import APIRouter, FastAPI

from .utils_router import router as utils
from .square_container_router import router as square_container

app = FastAPI(
    version="0.1.0",
    title="square_container title",
    description="Microservice that uses square_container",
    docs_url="/",
)

responses = {
    200: {"description": "Request was successful"},
    400: {"description": "Request was unsuccessful. Client error"},
    500: {"description": "Request was unsuccessful. Server error"},
}

app.include_router(square_container, prefix="/square_container", tags=["square_container"], responses=responses)
app.include_router(utils, prefix="/utils", tags=["utils"], responses=responses)
