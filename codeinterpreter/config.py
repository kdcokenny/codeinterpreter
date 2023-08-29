from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# .env file
load_dotenv(dotenv_path="./.env")


class CodeInterpreterAPISettings(BaseSettings):
    """CodeInterpreter API Config."""

    VERBOSE: bool = False

    OPENAI_API_KEY: Optional[str] = None
    CODEBOX_API_KEY: Optional[str] = None

    HISTORY_BACKEND: Optional[str] = None
    REDIS_URL: str = "redis://localhost:6379"
    POSTGRES_URL: str = "postgresql://postgres:jkASn12#s@20.219.154.180:5432"


settings = CodeInterpreterAPISettings()
