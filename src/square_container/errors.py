import logging
from typing import Any, Dict, Optional

from fastapi import HTTPException as FastHTTPException

logger = logging.getLogger()


class HTTPException(FastHTTPException):
    def __init__(self, status_code: int, detail: Any = None, headers: Optional[Dict[str, Any]] = None) -> None:
        logger.error(f"Status code: {status_code!r}, Detail: {detail!r}", exc_info=True)
        super().__init__(status_code=status_code, detail=detail, headers=headers)

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r}, detail={self.detail!r})"
