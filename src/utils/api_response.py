from typing import Any
from fastapi.responses import JSONResponse

class ApiResponse:
    @staticmethod
    def success(data: Any = None, message: str = "Success", status_code: int = 200):
        return JSONResponse(
            status_code= status_code,
            content={
                "status": "success",
                "message": message,
                "data": data
            }
        )
    
    @staticmethod
    def error(message: str, status_code:int):
        return JSONResponse(
            status_code=status_code,
            content={
                "status":"Error",
                "message":message,
                "data":None
            }
        )