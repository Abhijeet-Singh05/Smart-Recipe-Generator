from fastapi import APIRouter, UploadFile, File
from src.controllers.recipe import process_recipe_request


router = APIRouter()

@router.post("/analyse-food")
async def analyze_food_endpoint(file: UploadFile = File(...)):
    """
    Docstring for analyze_food_endpoint
    
    :param file: Description
    :type file: UploadFile
    Endpoint to upload an image
    """

    return await process_recipe_request(file)
