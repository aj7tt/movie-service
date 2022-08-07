#~/movie-service/app/api/controller.py#
import json
import time
import uuid
from datetime import datetime, timezone
from json import JSONDecodeError
from typing import Optional
from fastapi import APIRouter, Request
from starlette import status
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK
