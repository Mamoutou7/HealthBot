from app.graph.state import HealthBotState

from langgraph.types import interrupt

class PresentSummaryNode:

    def __call__(self, state: HealthBotState):

        interrupt(
            {
                "type": "show_summary",
                "summary": state["summary"]
            }
        )

        return state