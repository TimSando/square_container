import os
from pathlib import Path

DEBUG = os.environ.get("DEBUG", "False").upper() in ["TRUE", "ON"]

TEST_FILE_FOLDER = Path("/opt/working/src/tests/data")
