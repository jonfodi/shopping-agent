from enum import Enum
from typing import TypedDict, NotRequired, Required, Dict, List, Any

# Define a single shoe item
# ideally this would be data that a nike api would need to retrieve an item and process a payment
class ShoeItem(TypedDict):
    shoe_type: str
    price: float 
    size: str     
    color: str
    url: NotRequired[str]
    availability: NotRequired[str]
    description: NotRequired[str]
    id: NotRequired[str] # nike would give this. use for payment 

# make gender enum of either male or female
class Gender(Enum):
    MALE = "men"
    WOMAN = "women"

class ShoeType(Enum):
    AIR_FORCE_ONE = "air force one"
    AIR_JORDAN = "air jordan"
    AIR_MAX = "air max"


# Define the input state
class InputState(TypedDict, total=False):
    shoe_type: Required[str]
    size: Required[float]
    gender: Required[Gender]
    budget: NotRequired[int]
    color: NotRequired[str]

class ShoppingState(InputState):
    url: str
    shoes: List[ShoeItem]  # List of all extracted shoes
    extraction_status: NotRequired[str]  # Track extraction success/failure
    shoe_data: Dict[str, Any]