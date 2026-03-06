from app.services.llm_service import LLMService
from app.prompts.grading_prompt import GRADING_PROMPT
from app.graph.state import HealthBotState

from langchain_core.prompts import ChatPromptTemplate


class AnswerEvaluationNode:
    """
    LangGraph node responsible for evaluating the patient's answer.
    """

    def __init__(self):
        self.llm = LLMService().get_llm()

        self.prompt_template = GRADING_PROMPT

    def __call__(self, state: HealthBotState) -> HealthBotState:
        """
        Evaluate the patient's quiz response.

        Args:
            state (HealthBotState): Current workflow state.

        Returns:
            HealthBotState: Updated state containing evaluation results.
        """

        chain = self.prompt_template | self.llm

        evaluation = chain.invoke({
            "summary": state["summary"],
            "question": state["quiz_question"],
            "answer": state["patient_answer"],
        }).content

        return {
            **state,
            "explanation": evaluation
        }
