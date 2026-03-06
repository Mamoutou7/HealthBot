from typing import Optional, TypedDict

class HealthBotState(TypedDict):
    """
    Shared workflow state used by LangGraph nodes.

    Attributes:
        topic (Optional[str]): Health topic selected by the patient.
        search_results (Optional[str]): Raw search results retrieved from Tavily.
        summary (Optional[str]): Simplified explanation generated for the patient.
        quiz_question (Optional[str]): Quiz question generated from the summary.
        patient_answer (Optional[str]): Patient's answer to the quiz question.
        grade (Optional[str]): Evaluation result of the answer.
        explanation (Optional[str]): Detailed explanation of the evaluation.
        session_active (bool): Indicates whether the session is active.
    """
    topic: Optional[str]
    search_results: Optional[str]
    summary: Optional[str]
    quiz_question: Optional[str]
    patient_answer: Optional[str]
    grade: Optional[str]
    explanation: Optional[str]
    ready_for_quiz: Optional[bool]
    session_active: bool