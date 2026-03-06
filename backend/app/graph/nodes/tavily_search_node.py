from app.graph.state import HealthBotState
from app.services.tavily_service import TavilyService



class TavilySearchNode:
    """
    LangGraph node responsible for retrieving medical information.

    This node queries the Tavily search engine using the topic
    provided by the patient and stores the results in the workflow state.
    """

    def __init__(self,):
        self.search_service = TavilyService()

    def __call__(self,state: HealthBotState) -> HealthBotState:
        """
        Execute the search step of the workflow.

        Args:
            state (HealthBotState): Current workflow state.

        Returns:
            HealthBotState: Updated state including search results.
        """
        topic = state["topic"]
        results = self.search_service.search_medical(topic)

        return {
            **state,
            "results": results,
        }
