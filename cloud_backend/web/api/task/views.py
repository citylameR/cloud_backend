from fastapi import APIRouter
from starlette.status import HTTP_201_CREATED

from cloud_backend.queue.celery import run_celery_task
from cloud_backend.web.api.task.schema import Msg

router = APIRouter()


@router.post("/", response_model=str, status_code=HTTP_201_CREATED)
def test_celery(msg: Msg) -> str:
    """Test Celery worker.

    :param msg: message to publish to celery.
    :returns: task id
    """
    task = run_celery_task("test_celery", args=[msg.msg])
    return str(task.id)
