from typing import Any

from celery import Celery
from celery.result import AsyncResult

from cloud_backend.settings import settings

CELERY_APP_NAME = "cloud_backend.queue.worker"
celery_app = Celery(
    "cloud_backend",
    backend=str(settings.redis_url),
    broker=str(settings.rabbit_url),
)

celery_app.conf.update(
    result_expires=settings.celery_task_result_expires,
    task_serializer="json",
    accept_content=["json", "yaml", "msgpack", "application/x-yaml"],
    result_serializer="json",
    task_track_started=True,
    task_acks_late=True,
    task_reject_on_worker_lost=True,
)

celery_app.conf.task_routes = {
    f"{CELERY_APP_NAME}.test_celery": settings.queue_name,
}


def get_celery_task(task_id: str) -> AsyncResult:
    """
    Returns AsyncResult instance connected to the task with the provided task_id.

    :param task_id: Unique id of the Celery task.
    :returns: AsyncResult instance for the task.
    """
    return AsyncResult(id=task_id, app=celery_app)


def run_celery_task(
    task: str,
    args: Any = None,
    kwargs: Any = None,
    serializer: str = "json",
) -> AsyncResult:
    """
    This function is used to run a celery task.

    :param task: Name of the task to run.
    :param args: List of positional arguments to pass to the task.
    :param kwargs: Dictionary of keyword arguments to pass to the task.
    :param serializer: Serializer to use. Default is 'json'.
    :return: It returns a AsyncResult instance.
    """
    return celery_app.send_task(
        f"{CELERY_APP_NAME}.{task}",
        args=args,
        kwargs=kwargs,
        serializer=serializer,
    )


if __name__ == "__main__":
    celery_app.start()
