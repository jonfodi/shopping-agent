import asyncio
import logging
import os
from typing import Any, Dict, List, Union
from tavily import TavilyClient
import dotenv
from ..classes import ShoppingState

dotenv.load_dotenv()
logger = logging.getLogger(__name__)

# should extract all the shoes from the urls
# should return a dictionary of shoe data 
# {shoe_type: x, size: y, color: z, price: a}
# then processor will use an LLM to determine the best shoe based on input data


class Extractor:

    def __init__(self) -> None:
        self.tavily_client = TavilyClient()
    
    def extract(self, state: ShoppingState) -> ShoppingState:
        print("extracting")
        url = state.get("url")
        shoe_data = state.get("shoe_data")
        for shoe in shoe_data:
            print(shoe.get("url"))
        print("extraction complete")

        shopping_state = {
            "shoe_type": "test",
            "size": "test",
            "color": "test",
            "price": "test"
        }
        return shopping_state

    def run(self, state: ShoppingState):
        print("running extract")
        return self.extract(state)

    def extract_from_url(self, url: str) -> str:
        response = self.tavily_client.extract(urls=url)
        return response
    
def process_extraction(response: str) -> dict:
    pass