import os
from tavily import TavilyClient
from agents import function_tool
from dotenv import load_dotenv

load_dotenv()
tavily_api_key = os.getenv("TAVILY_API_KEY")
max_search_results = os.getenv("MAX_SEARCH_RESULTS", 3)

if not tavily_api_key:
    raise ValueError("TAVILY_API_KEY not found in environment variables.")


@function_tool
def web_search_tool(query: str, max_results: int = max_search_results) -> list[dict]:
    """ Perform a web search using the Tavily API and return the results """
    client = TavilyClient(tavily_api_key)
    response = client.search(query=query, max_results=max_results)

    results = []
    for result in response["results"]:
        results.append({
            "url": result["url"],
            "title": result["title"],
            "content": result["content"]
        })
    return results