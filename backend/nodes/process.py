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

    def process(self, shopping_state: ShoppingState) -> ShoppingState:
        print("processing")
        print(shopping_state.get("enhanced_shoe_data"))

        return shopping_state
    
    def run(self, shopping_state: ShoppingState) -> ShoppingState:
        return self.process(shopping_state)
    
    def rank_shoe_options(self, shopping_state: ShoppingState) -> Dict[str, Any]:
        print(shopping_state.get("enhanced_shoe_data"))
        
        # print input state data from shopping state (shopping inherits from input state)
        gender = shopping_state.get("gender")
        print(gender)

        return {}