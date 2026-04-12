import logging

logger = logging.getLogger(__name__)

def print_log(msg: str) -> None:
    logger.info(msg)

def print_err(msg: str) -> None:
    logger.error(msg)
