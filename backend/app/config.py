from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """
    Application configuration settings.

    This class loads configuration values from environment variables
    and provides strongly typed access to application settings

    Attributes:
    openai_api_key (str): API key used to authenticate with OpenAI services.
    tavily_api_key (str): API key used for Tavily search engine queries.
    llm_model (str): Default language model used by the application.
    temperature (float): Sampling temperature for the language model.
    """
    API_KEY: str
    API_SECRET: str
    openai_api_key: str
    tavily_api_key: str

    llm_model: str = "gpt-4o-mini"
    temperature: float = 0.2


settings = Settings()