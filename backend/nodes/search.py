import logging
import os
import dotenv
from ..classes import InputState, ResearchState
from tavily import TavilyClient


dotenv.load_dotenv()


from ..classes import ResearchState

logger = logging.getLogger(__name__)

class Searcher:
    def __init__(self) -> None:
        self.tavily_client = TavilyClient()

    def initial_search(self, state: InputState) -> ResearchState:
        print(state.get("color"))
        print("initial search")

        prompt = construct_tavily_search_prompt(state)

        results = self.tavily_client.search(query=prompt, include_domains=["nike.com"])
        for result in results.get("results", []):
            if not result.get("content") or not result.get("url"):
                continue
                
            url = result.get("url")
            title = result.get("title", "")
            print(url)
            print(title)

        research_state = {
           "url": "test"
        }
        print("initial search complete")
        return research_state
    
    
    def run(self, state: InputState) -> ResearchState:
        print("running search")
        return self.initial_search(state)




def construct_tavily_search_prompt(state: InputState) -> str:
    prompt = f"""
    You are a shopping assistant for the nike store. Your job is to find the best shoes for the user based on the provided data.
    Required fields:
    Shoe type: {state.get("shoe_type")}
    Size: {state.get("size")}

    Optional fields:
    Color: {state.get("color")}
    Budget: {state.get("budget")}

    Find the URL that contains the shoes that most closely match the user's requirements.
    """
    return prompt

def parse_tavily_response(response: dict) -> list[str]:
    urls = []
    for result in response.get("results", []):
        urls.append(result.get("url"))
    return urls