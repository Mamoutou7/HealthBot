from pydantic import BaseModel
from typing import Optional


class HealthBotStateModel(BaseModel):
    """
    Strongly typed representation of the HealthBot workflow state.

    This model is useful for validation, debugging, and logging
    of the workflow state in production systems.
    """

    topic: Optional[str] = None
    search_results: Optional[str] = None
    summary: Optional[str] = None
    quiz_question: Optional[str] = None
    patient_answer: Optional[str] = None
    grade: Optional[str] = None
    explanation: Optional[str] = None
    session_active: bool = True