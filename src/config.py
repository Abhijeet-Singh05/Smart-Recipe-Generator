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
   DB_NAME = "chefDB"
   MONGODB_URL = os.getenv("MONGODB_URL") 

config = Config()