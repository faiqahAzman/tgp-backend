from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "TGP Backend"
    API_V1_STR: str = "/api/v1"
    COUNTRY_CODE: str = "MYS"  # ISO3 code for Malaysia
    WORLDBANK_API_BASE_URL: str = "https://api.worldbank.org/v2"
    KAFKA_BOOTSTRAP_SERVERS: str = "localhost:9092"
    KAFKA_TOPIC_PREFIX: str = "risk-indicators"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]  # React frontend

    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
