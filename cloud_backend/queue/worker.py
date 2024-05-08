import logging
from time import sleep

from cloud_backend.queue.celery import celery_app

logger = logging.getLogger("workers")
logger.propagate = False


@celery_app.task(acks_late=True)
def test_celery(value: str) -> str:
    """
    A Celery task that takes a string, waits for 1 second, and returns the same string.

    :param value: The string input
    :type value: str
    :return: The same string that was received as input
    :rtype: str
    """
    sleep(1)
    return f"{value}"
