import asyncio
import logging
import os
from typing import Any, Dict, List, Union
import dotenv

dotenv.load_dotenv()

from ..classes import InputState, ShoppingState


logger = logging.getLogger(__name__)

class Processor:
    def __init__(self):
        pass

    def process(self, shopping_state: ShoppingState, input_state: InputState) -> ShoppingState:
        print("processing")
        print(shopping_state)
        print(input_state)
        shoe_recommendations = {}
        shoe_recommendations = self.rank_shoe_options(shopping_state, input_state)
        shopping_state["shoe_reccomendations"] = shoe_recommendations
        return shopping_state
    
    def run(self, shopping_state: ShoppingState, input_state: InputState) -> ShoppingState:
        return self.process(shopping_state, input_state)
    
    def rank_shoe_options(self, shopping_state: ShoppingState, input_state: InputState) -> Dict[str, Any]:
        for url, shoe_info in shopping_state.get("enhanced_shoe_data").items():
            print(shoe_info)
            print(url)
            print("*"*100)
        return {}