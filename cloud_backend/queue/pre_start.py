import logging
import time

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from cloud_backend.queue.worker import logger
from cloud_backend.settings import settings


@retry(
    stop=stop_after_attempt(settings.max_tries),
    wait=wait_fixed(settings.wait_seconds),
    before=before_log(logger, logging.DEBUG),
    after=after_log(logger, logging.DEBUG),
)
def init() -> None:
    """
    Retryable initialization function.

    :raises Exception: Any exception that occurs during sleep.
    """
    try:
        time.sleep(1)
    except Exception as ex:
        logger.error(ex)
        raise ex


def main() -> None:
    """Starts and initializes the service."""
    logger.info("Initializing service")
    init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()
