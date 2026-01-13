from fastapi import UploadFile
from datetime import datetime

from src.services.ai_service import generate_recipe
from src.services.cloudinary import upload_to_cloud

from src.databse import get_db

from src.utils.api_error import apiError
from src.utils.api_response import apiResponse

from src.models.ingredient_model import AnalyzeFoodResponse, RecipeData


async def process_recipe_request(file: UploadFile):
    """
    Docstring for process_recipe_request
    
    :param file: Description
    :type file: UploadFile


    """

    # validation
    if not file.content_type.startswith("image/"):
        raise apiError(
            400,
            "file must be an image"
        )
    
    # read file
    file_content = await file.read()

    # upload on cloudinary
    cloud_data = upload_to_cloud(file_content)

    # validate 
    if not cloud_data:
        raise apiError(500,"failed to upload")

    # Call AI
    recipe_data = await generate_recipe(file_content,file.content_type)
    if not recipe_data:
        raise apiError(500,"geimin failed to response")

    # write to mongoDB
    try:
        db_record = AnalyzeFoodResponse(
            image_url= cloud_data,
            #recipe= RecipeData(**recipe_data)
        )
    except Exception as e:
        raise apiError(500,"Validation Error")
    

    db = get_db()

    result = db["recipe"].insert_one(
        db_record.model_dump()
    )


    return apiResponse(
        message="Recipe created successfully",
        data = {
            **db_record.model_dump(by_alias=True),
            "id":str(result.inserted_id)
        }
    ).dict()

