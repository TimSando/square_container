import os
import uvicorn

from src.api import app
from src.square_container.setup_logging import setup_logging

config = setup_logging(path="/opt/working/logging.yaml")

# Initialize the FastAPI application

if __name__ == "__main__":
    uvicorn.run(
        "api:app",
        port=int(os.environ["FASTAPI_PORT"]),
        host="0.0.0.0",
        reload=os.environ.get("DEBUG", "FALSE").upper() in ["T", "TRUE"],
        log_config=config,
    )
