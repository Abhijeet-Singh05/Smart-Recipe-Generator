from pydantic import BaseModel, Field
from typing import List

class RecipeData(BaseModel):
    title: str = Field(..., description="Dish Name")
    time: str = Field(..., description="Cooking time")
    difficulty: str = Field(..., description="Difficulty Level")
    ingredientds: List[str] = Field(..., description="List of ingredients")
    instructions: List[str] = Field(..., description="Instructions")
    youtube_url: str = Field(..., description="Link to a tutorial")

class AnalyzeFoodResponse(BaseModel):
    image_url : str
    recipe: RecipeData

