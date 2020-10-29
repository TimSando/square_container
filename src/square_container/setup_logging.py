import logging.config
import os

import yaml


def setup_logging(path=os.path.join(os.path.dirname(__file__), "logging.yaml"), default_level=logging.INFO):
    """Setup logging configuration
    
    Args:
        path (str, optional): [description]. Defaults to 'logging.yaml'.
        default_level ([type], optional): [description]. Defaults to logging.INFO.
    """
    if os.path.exists(path):
        with open(path, "rt") as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
