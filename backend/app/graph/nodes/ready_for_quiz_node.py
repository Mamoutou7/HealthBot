from app.graph.state import HealthBotState
from langgraph.types import interrupt


class ReadyForQuizNode:

    def __call__(self, state: HealthBotState):

        ready = interrupt(
            {
                "type": "ready_for_quiz",
                "message": "Are you ready for a comprehension quiz?"
            }
        )

        return {**state, "ready_for_quiz": ready}