import logging

logger = logging.getLogger()


def demo(image):
    logger.info(image)
    return {"message": "Hello World"}


def demo2(string):
    logger.info(string)
    return {"summary": {"message": "Goodbye World", "sleep": True}}
