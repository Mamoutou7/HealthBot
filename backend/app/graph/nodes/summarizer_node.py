from langchain_core.prompts import ChatPromptTemplate
from app.services.llm_service import LLMService
from app.prompts.summarization_prompt import SUMMARIZATION_PROMPT
from app.graph.state import HealthBotState



class SummarizerNode:
    """
    LangGraph node responsible for generating a patient-friendly summary.

    This node transforms raw medical information into a simplified
    explanation that patients can easily understand.
    """

    def __init__(self):
        self.llm = LLMService().get_llm()
        self.prompt_template = SUMMARIZATION_PROMPT

    def __call__(self, state: HealthBotState) -> HealthBotState:
        """
        Generate a simplified summary of the retrieved medical information.

        Args:
            state (HealthBotState): Current workflow state.

        Returns:
            HealthBotState: Updated state including the generated summary.
        """

        chain = self.prompt_template | self.llm

        summary = chain.invoke({
            "context": state["search_results"]
        }).content

        return {
            **state,
            "summary": summary
        }
