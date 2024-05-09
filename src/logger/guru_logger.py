from typing import Optional

from loguru import logger

logger.add(
    "critical_log.log", level="CRITICAL", format="{time:HH:mm:ss} | {message}"
)


def info(msg):
    logger.info(msg)


def error(msg, e: Optional[Exception] = None):
    if e is not None:
        logger.opt(exception=e).error(msg, e)
    else:
        logger.opt(exception=True).error(msg)


def warning(msg):
    logger.warning(msg)


def critical(msg):
    logger.critical(msg)
