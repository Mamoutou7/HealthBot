from langchain_openai import ChatOpenAI
from app.config import settings



class LLMService:
    def __init__(self) -> None:
        self.llm = ChatOpenAI(
            model=settings.llm_model,
            temperature=settings.temperature,
            api_key=settings.openai_api_key,
        )

    def get_llm(self) -> ChatOpenAI:
        return self.llm