import logging
import os

from fastapi import APIRouter, File, Query, UploadFile
from fastapi.responses import FileResponse

from src.square_container.errors import HTTPException
from src.square_container.settings import TEST_FILE_FOLDER
from src.square_container.square_container import demo, demo2

from .square_container_schema import (square_container_demo,
                                              square_container_demo2)

logger = logging.getLogger()

router = APIRouter()


@router.post("/demo", response_model=square_container_demo)
async def demo_endpoint(doc_upload: UploadFile = File(..., description="File that we want to upload and run through the demo 1 service")):

    return demo(doc_upload)


@router.post("/demo2", response_model=square_container_demo2)
async def demo2_endpooint(input_variable: str = Query("Empty", description="A string that you want to pass through to your function. Defaults to Empty")
):
    return demo2(input_variable)

@router.get(
    "/download/{filename}",
    description="Downloads a file based on the filename provided",
    responses={
        200: {"description": "File is available for download"},
    })
async def download_demo(filename: str):
    """Downloads a trained classification model"""
    if not os.path.exists(os.path.join(TEST_FILE_FOLDER, filename)):
        raise HTTPException(
            status_code=404,
            detail={"name": "FileDoesntExistError", "message": f"Could not find file {filename}", "code": 1001},
        )
    return FileResponse(
        path=os.path.join(TEST_FILE_FOLDER, filename),
        headers={
            "content-disposition": f"attachment; filename={filename}",
            "content-type": "application/octet-stream",
        },
    )
