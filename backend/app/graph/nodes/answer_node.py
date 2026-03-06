from langgraph.types import interrupt

from backend.app.graph.state import HealthBotState


class AskAnswerNode:

    def __call__(self, state:HealthBotState):

        answer = interrupt(
            {
                "type": "quiz",
                "question": state["quiz_question"]
            }
        )

        return {**state, "patient_answer": answer}