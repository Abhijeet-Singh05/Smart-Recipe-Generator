import os
from dotenv import load_dotenv

# to load .env file
load_dotenv

# to assign values here globally so that all files can you them
# these all are constant values
class Config:
   
   # we use getenv() to get values from .env file. 
   # getenv() will return none if the variable in .env is empty.
   PORT = os.getenv("PORT") # port 
   DB_NAME = "chefDB" # database name
   MONGODB_URL = os.getenv("MONGODB_URL") # mongoDB url
   CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
   CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
   CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
   GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
 


config = Config()