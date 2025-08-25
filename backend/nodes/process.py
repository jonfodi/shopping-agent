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

    def process(self, state: ShoppingState) -> ShoppingState:
        pass
    
    def run(self, state: ShoppingState) -> ShoppingState:
        return self.process(state)