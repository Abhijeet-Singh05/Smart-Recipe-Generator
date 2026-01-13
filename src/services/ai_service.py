import json
from google import genai
from google.genai import types
from src.config import Config
from src.utils.api_error import apiError

client = genai.Client(api_key=Config.GEMINI_API_KEY)

def generate_recipe(file_bytes,mime_types):
    """
    Docstring for generate_recipe
    
    :param file_bytes: Description
    :param mime_types: Description

    Send image to gemini
    """

    prompt = """
        Analyze this image. Identify the food or ingredients.
        1. Create a detailed recipe based on what you see.
        2. Generate a YouTube Search URL for this specific dish.
    
        Strictly output VALID JSON with this structure:
        {
            "title": "Recipe Title",
            "time": "XX mins",
            "difficulty": "Easy/Medium/Hard",
            "ingredients": ["item 1", "item 2"],
            "instructions": ["Step 1", "Step 2"],
            "youtube_url": "https://www.youtube.com/results?search_query=..."
        }
    """

    try:
        res = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[
                types.Part.from_text(text=prompt),
                types.Part.from_bytes(data=file_bytes,mime_type=mime_types)
            ],
            config = types.GenerateContentConfig(
                response_mime_type= 'application/json'
            )

        )

        return json.loads(res.text)
    
    except Exception as e:
        raise apiError(500,"Gemini AI error")