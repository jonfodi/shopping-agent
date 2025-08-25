import logging
import dotenv
from ..classes import InputState, ShoppingState
from tavily import TavilyClient

dotenv.load_dotenv()
logger = logging.getLogger(__name__)

# IMPROVEMENTS 
# search multiple urls 
# must have async capability

class Searcher:
    def __init__(self) -> None:
        self.tavily_client = TavilyClient()

    def initial_search(self, state: InputState) -> ShoppingState:
        query = construct_tavily_search_prompt(state)
        results = self.search_nike_store(query=query)
        url_to_extract = get_url_to_extract(results)
        
        shopping_state = {
           "url": url_to_extract
        }
        print("initial search complete")
        return shopping_state
    
    def search_nike_store(self, query: str) -> dict:  # Return dict, not list[str]
        include_domains = ["nike.com"]
        results = self.tavily_client.search(query=query, include_domains=include_domains, max_results=5)
        return results
    
    def run(self, state: InputState) -> ShoppingState:
        print("running search")
        return self.initial_search(state)

def construct_tavily_search_prompt(state: InputState) -> str:
    shoe_type = state.get("shoe_type")
    size = state.get("size")
    color = state.get("color", "")
    budget = state.get("budget", "")
    
    color_text = f" {color}" if color else ""
    budget_text = f" under ${budget}" if budget else ""
    
    prompt = f"""
    Find Nike product detail pages (individual shoe pages) for {shoe_type}{color_text} shoes{budget_text} available in size {size}.
    
    IMPORTANT: Only return URLs that show a SINGLE specific shoe model with size/color options, NOT search results or category pages.
    
    Look for Nike.com URLs that contain specific product codes (like /t/shoe-name-product-code/XXXXXXX-XXX format).
    
    Avoid URLs containing:
    - /w/ (category pages)
    - /search/ (search results)
    - Multiple shoes on one page
    
    Target URLs should show:
    - One specific shoe model
    - Size selector dropdown
    - Color/variant options for that model
    - Add to cart functionality
    """
    return prompt

def get_url_to_extract(results: dict) -> list[str]:
    urls = []
    for result in results.get("results", []):
        if not result.get("url"):
            continue
        url = result.get("url")
        urls.append(url)
    return urls