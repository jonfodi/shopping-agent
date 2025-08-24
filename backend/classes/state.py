from typing import TypedDict, NotRequired, Required, Dict, List, Any

#Define the input state
class InputState(TypedDict, total=False):
    company: Required[str]

class ResearchState(InputState):
    url: str