from typing import Dict, List, Optional

from fastapi import FastAPI
from pydantic import BaseModel


class square_container_demo(BaseModel):
    message: str

class square_container_demo2_partial(BaseModel):
    message: str
    sleep: bool

class square_container_demo2(BaseModel):
    summary: square_container_demo2_partial
