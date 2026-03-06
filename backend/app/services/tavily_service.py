from tavily import TavilyClient
from app.config import settings


class TavilyService:
    """
    Service responsible for retrieving medical information
    from the Tavily search engine.

    This service abstracts external search operations and
    returns formatted results suitable for downstream processing.
    """
    def __init__(self):
        self.client = TavilyClient(
            api_key=settings.tavily_api_key
        )

    def search_medical(self, query: str) -> str:
        """
        Perform a search query using Tavily and format the results.
        Args:
            query (str): Medical topic or condition to search for.
        Returns:
            str: Concatenated string containing relevant search results.
        """
        results = self.client.search(
            query=query,
            max_results=5
        )

        formatted = "\n".join(
            f"{r['title']} - {r['content']}"
            for r in results["results"]
        )

        return formatted
