from itertools import chain

from langchain_core.prompts import ChatPromptTemplate
from app.services.llm_service import LLMService
from app.prompts.quiz_prompt import QUIZ_PROMPT
from app.graph.state import HealthBotState


class QuizGenerationNode:
    """
    LangGraph node responsible for generating a quiz question.

    The quiz is used to assess the patient's understanding
    of the summarized medical explanation.
    """

    def __init__(self):
        self.llm = LLMService().get_llm()
        self.prompt_template = QUIZ_PROMPT

    def __call__(self, state: HealthBotState) -> HealthBotState:
        """
        Generate a quiz question from the summary.

        Args:
            state (HealthBotState): Current workflow state.

        Returns:
            HealthBotState: Updated state containing the quiz question.
        """
        chain = self.prompt_template | self.llm

        question = chain.invoke({
            "summary": state["summary"],
        }).content

        return {
            **state,
            "quiz_question": question
        }
