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
        pass
    
    def run(self, shopping_state: ShoppingState, input_state: InputState) -> ShoppingState:
        return self.process(shopping_state, input_state)