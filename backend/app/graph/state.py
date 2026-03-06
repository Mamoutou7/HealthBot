from typing import Optional, TypedDict

class HealthBotState(TypedDict):
    """
    Represents the shared state of the HealthBot workflow.

    This state object is passed between nodes in the LangGraph workflow.
    Each node reads and updates parts of the state.

    Attributes:
        topic (Optional[str]): Health topic selected by the patient.
        search_results (Optional[str]): Raw search results retrieved from Tavily.
        summary (Optional[str]): Simplified explanation generated for the patient.
        quiz_question (Optional[str]): Quiz question generated from the summary.
        user_answer (Optional[str]): Patient's answer to the quiz question.
        grade (Optional[str]): Evaluation result of the answer.
        explanation (Optional[str]): Detailed explanation of the evaluation.
        session_active (bool): Indicates whether the session is active.
    """
    topic: Optional[str]
    search_results: Optional[str]
    summary: Optional[str]
    quiz_question: Optional[str]
    user_answer: Optional[str]
    grade: Optional[str]
    explanation: Optional[str]
    session_active: bool