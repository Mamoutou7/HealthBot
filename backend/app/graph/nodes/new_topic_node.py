from app.graph.state import HealthBotState
from langgraph.types import interrupt


class NewTopicNode:
    """
    Ask if the patient wants to learn about another topic.
    """

    def __call__(self, state):
        decision = interrupt(
            {
                "type": "continue",
                "message": "Would you like to learn about another topic?"
            }
        )

        return {**state, "session_active": decision}