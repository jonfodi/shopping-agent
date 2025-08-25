import logging
from tavily import TavilyClient
import dotenv

from backend.classes.state import InputState
from ..classes import ShoppingState
from typing import Any, Dict

dotenv.load_dotenv()
logger = logging.getLogger(__name__)

class Crawler:
    def __init__(self):
        self.tavily_client = TavilyClient()

    def crawl(self, state: InputState) -> Dict[str, Any]:

        shoe_data = {}
        crawl_instructions = create_crawl_instructions(state)

        response = self.crawl_nike_with_tavily(state, crawl_instructions)
        return shoe_data
    
    def crawl_nike_with_tavily(self, state: InputState, crawl_instructions: str) -> Dict[str, Any]:

        url = f"https://www.nike.com/{state.gender}"
        response = self.tavily_client.extract(
            urls=url,
            instructions=crawl_instructions,
            max_results=15,
            max_breadth=2,
            include_raw_content=True,
        )
        return response

    def run(self, state: ShoppingState) -> ShoppingState:
        return self.crawl(state)

def create_crawl_instructions(state: InputState) -> str:
    instructions=f"""
    Find individual nike {state.shoe_type} shoe product pages that start with '/t/' in the URL. 
    Look for specific shoe models with names, prices, and product codes like 'FD2597-602' or 'HJ5940-071'. 
    All shoes should be in the '{state.gender} 's' category and under size {state.size}"
    """
    return instructions
    
