import os
import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import watchtower
import boto3
import logging
from dotenv import load_dotenv

load_dotenv()
access_key = os.getenv('AWS_ACCESS_KEY_ID')
access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
access_key = os.getenv('AWS_DEFAULT_REGION')

cloudwatch_handler = watchtower.CloudWatchLogHandler(log_group='jcard-backend', stream_name='uvicorn-logs')
logger = logging.getLogger('uvicorn')
logger.setLevel(logging.INFO)
logger.addHandler(cloudwatch_handler)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        logger.info(f"Request: {request.method} {request.url}")
        response = await call_next(request)

        process_time = time.time() - start_time
        logger.info(f"Response: status_code={response.status_code}, process_time={process_time:.4f}s")

        return response