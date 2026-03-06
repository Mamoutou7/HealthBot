from pydantic import BaseModel


class QuizQuestion(BaseModel):
    """
    Represents a generated quiz question.

    Attributes:
        question (str): Quiz question related to the medical explanation.
    """

    question: str


class QuizEvaluation(BaseModel):
    """
    Represents the evaluation of a patient's answer.

    Attributes:
        grade (str): Result of the evaluation (Correct / Incorrect).
        explanation (str): Explanation supporting the evaluation.
    """

    grade: str
    explanation: str