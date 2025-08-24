import asyncio
import logging
import os
from typing import Any, Dict, List, Union
from langchain_tavily import TavilySearch
import dotenv

dotenv.load_dotenv()

from ..classes import ShoppingState

logger = logging.getLogger(__name__)


class Extractor:

    def __init__(self) -> None:
        self.tavily_client = TavilySearch()
    
    def extract(self, state: ShoppingState):
        print("extracting")
        url = state.get("url")
        print(url)
        print("extraction complete")
    
    def run(self, state: ShoppingState):
        print("running extract")
        return self.extract(state)
