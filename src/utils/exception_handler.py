from fastapi import Request
from fastapi.responses import JSONResponse
from src.utils.api_error import CustomException
from src.utils.api_response import ApiResponse

async def custom_exception_handler(request: Request, exc: CustomException):
    return ApiResponse.error(message=exc.message, status_code=exc.status_code)


async def global_exception_handler(request: Request, exc: Exception):
    print(f"Error: {str(exc)}")
    return ApiResponse.error(message="Internal Server Error", status_code=500)