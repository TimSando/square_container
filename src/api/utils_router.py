import logging

from fastapi import APIRouter

logger = logging.getLogger()

router = APIRouter()

# Heartbeat endpoint
@router.get("/heartbeat", description="Checks that the microservice is still up and running")
async def heartbeat():
    """Endpoint for checking the status of the microservice

    """

    logger.info("Check service is up and running")
    return {}
