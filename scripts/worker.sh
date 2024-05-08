#! /usr/bin/env bash
set -e

python3 cloud_backend/queue/pre_start.py

if [ -n "${RUN}" ]; then
  ${RUN}
else
  celery -A cloud_backend.queue.worker worker -l info -Q ${CLOUD_BACKEND_QUEUE_NAME_QUEUE_NAME} -c 1
fi
