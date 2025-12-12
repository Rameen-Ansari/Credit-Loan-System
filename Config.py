from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    PROJECT_NAME: str="CREDIT/LOAN BACKEND"
    SECRET_KEY: str="SECRET_KEY - CHANGE THIS"
    ACCESS_TOKEN_EXPIRE_MINUTES: int=60*24
    
    class config:
        env_file=".env"

settings=Settings()
