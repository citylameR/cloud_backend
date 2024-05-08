from fastapi.routing import APIRouter

from cloud_backend.web.api import docs, monitoring, redis, task

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(docs.router)
api_router.include_router(redis.router)
api_router.include_router(task.router)
