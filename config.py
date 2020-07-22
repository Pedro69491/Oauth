from os import getenv # get environment variables
from dotenv import load_dotenv  # load configuration from .env 

load_dotenv() # it opens the .env

class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

