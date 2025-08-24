from typing import TypedDict, NotRequired, Required, Dict, List, Any

#Define the input state
class InputState(TypedDict, total=False):
    shoe_type: Required[str]
    size: Required[float]
    budget: NotRequired[int]
    color: NotRequired[str]


class ShoppingState(InputState):
    url: list[str]
    price: float
    shoe_type: str
    size: float
    color: str