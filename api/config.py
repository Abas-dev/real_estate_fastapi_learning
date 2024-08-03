import pathlib
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Setting(BaseSettings):
    DB_URL: str

    class Config: 
        env_file = f"{pathlib.Path(__file__).resolve().parent}/.env"

def get_settings(): 
    return Setting()

get_settings()   