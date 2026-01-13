import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestErrorModel
from starlette.exceptions import HTTPException 

# Import route
from src.routes.route import router as recipe_router

# Import exception handlers
from src.utils.api_error import apiError
from src.utils.exception_handler import api_error_handler, generic_exception_handler

# Initializing APP
app = FastAPI(title="ChefAI",version="1.0")

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]   
)

# Error handling
app.add_exception_handler(apiError,api_error_handler)
app.add_exception_handler(Exception,generic_exception_handler)


# routes
app.include_router(recipe_router)

# root route
@app.get("/")
def home():
    return {
        "status": "online",
        "message": "ChefAP API is running"
    }

