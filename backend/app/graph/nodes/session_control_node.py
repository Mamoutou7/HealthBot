from app.graph.state import HealthBotState


class SessionControlNode:
    """
    Node responsible for controlling the HealthBot session lifecycle.

    This node determines whether the workflow should continue
    or reset for a new topic.
    """

    def __call__(self, state: HealthBotState) -> HealthBotState:
        """
        Manage the session lifecycle.

        Args:
            state (HealthBotState): Current workflow state.

        Returns:
            HealthBotState: Updated session state.
        """

        if not state.get("session_active", True):
            return {
                "topic": None,
                "search_results": None,
                "summary": None,
                "quiz_question": None,
                "patient_answer": None,
                "grade": None,
                "explanation": None,
                "session_active": False,
            }

        return state