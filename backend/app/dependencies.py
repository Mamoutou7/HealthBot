from functools import lru_cache
from app.graph.healthbot_graph import HealthBotGraph


@lru_cache
def get_healthbot_graph() -> HealthBotGraph:
    """
    Provide a singleton instance of the HealthBotGraph.

    Using caching ensures that the workflow graph is only compiled
    once during the application lifecycle.

    Returns:
        HealthBotGraph: Initialized workflow graph.
    """

    return HealthBotGraph()