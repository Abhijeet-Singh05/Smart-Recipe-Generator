class CustomException(Exception):
    """
    Docstring for CutomException
    Base class for custom API exceptions
    """

    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code

class ResourceNotFound(CustomException):
    def __init__(self,message="Resource not found!"):
        super().__init__(message,status_code=404)

class ExternalServiceException(CustomException):
    def __init__(self, message="External service error!!"):
        super().__init__(message, status_code=503)