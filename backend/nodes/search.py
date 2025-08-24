import logging
import dotenv
from ..classes import InputState, ShoppingState
from tavily import TavilyClient

dotenv.load_dotenv()
logger = logging.getLogger(__name__)

class Searcher:
    def __init__(self) -> None:
        self.tavily_client = TavilyClient()

    def initial_search(self, state: InputState) -> ShoppingState:
        query = construct_tavily_search_prompt(state)
        results = self.search_nike_store(query=query)
        urls_to_extract = get_urls_to_extract(results)
        
        shopping_state = {
           "url": urls_to_extract
        }
        print("initial search complete")
        return shopping_state
    
    def search_nike_store(self, query: str) -> dict:  # Return dict, not list[str]
        include_domains = ["nike.com"]
        results = self.tavily_client.search(query=query, include_domains=include_domains)
        return results
    
    def run(self, state: InputState) -> ShoppingState:
        print("running search")
        return self.initial_search(state)

def construct_tavily_search_prompt(state: InputState) -> str:
    prompt = f"""
    You are a shopping assistant for the nike store...
    Required fields:
    Shoe type: {state.get("shoe_type")}
    Size: {state.get("size")}
    
    Optional fields:
    Color: {state.get("color")}
    Budget: {state.get("budget")}
    
    Find the URL that contains the shoes that most closely match the user's requirements.
    """
    return prompt

def get_urls_to_extract(results: dict) -> list[str]:
    urls = []
    for result in results.get("results", []):
        if not result.get("url"):
            continue
        url = result.get("url")
        urls.append(url)
    return urls