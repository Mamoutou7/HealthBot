from app.graph.state import HealthBotState
from langgraph.types import interrupt


class TopicNode:
    """
    Normalize the topic provided by the patient.
    """

    def __call__(self, state: HealthBotState) -> HealthBotState:
        """
        Ask the patient which health topic they want to learn about.

        Args:
            state (HealthBotState): Current workflow state.

        Returns:
            HealthBotState: Updated state with normalized topic.
        """

        topic = interrupt(
            {
                "type": "topic",
                "message": "What health topic would you like to learn about?"
            }
        )

        return {**state, "topic": topic}