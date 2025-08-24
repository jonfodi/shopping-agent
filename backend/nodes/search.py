import logging
import os
from langchain_tavily import TavilySearch
from ..classes import InputState, ResearchState

import dotenv

dotenv.load_dotenv()


from ..classes import ResearchState

logger = logging.getLogger(__name__)

class Searcher:
    def __init__(self) -> None:
        self.tavily_client = TavilySearch()

    def initial_search(self, state: InputState) -> ResearchState:
        print("initial search")
        research_state = {
           "url": "test"
        }
        print("initial search complete")
        return research_state
    
    
    def run(self, state: InputState) -> ResearchState:
        print("running search")
        return self.initial_search(state)




