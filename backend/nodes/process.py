import asyncio
import logging
import os
from typing import Any, Dict, List, Union
import dotenv

dotenv.load_dotenv()

from ..classes import InputState, ResearchState

from ..classes import ResearchState

logger = logging.getLogger(__name__)

class Processor:
    def run(self, state: InputState) -> ResearchState:
        pass