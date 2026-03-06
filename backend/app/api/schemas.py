from pydantic import BaseModel
from typing import Optional


class TopicRequest(BaseModel):
    """
    Request model used to start a learning session.
    """

    topic: str


class AnswerRequest(BaseModel):
    """
    Request model used when the patient submits a quiz answer.

    Attributes:
        topic (str): Original health topic.
        summary (str): Generated explanation.
        quiz_question (str): Question asked the patient.
        patient_answer (str): Patient's answer.
    """

    topic: str
    summary: str
    quiz_question: str
    patient_answer: str


class HealthBotResponse(BaseModel):
    """
    Standard response returned by HealthBot endpoints.

    Attributes:
        topic (Optional[str]): Selected health topic.
        summary (Optional[str]): Patient-friendly explanation.
        quiz_question (Optional[str]): Quiz question generated.
        grade (Optional[str]): Evaluation result.
        explanation (Optional[str]): Explanation of the evaluation.
    """

    topic: Optional[str] = None
    summary: Optional[str] = None
    quiz_question: Optional[str] = None
    grade: Optional[str] = None
    explanation: Optional[str] = None


class ChatRequest(BaseModel):
    topic: str