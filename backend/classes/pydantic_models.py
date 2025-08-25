from pydantic import BaseModel
from backend.classes.state import Gender
from enum import Enum

class ShoeType(str, Enum):
    AIR_FORCE_ONE = "air force one"
    AIR_JORDAN = "air jordan"
    AIR_MAX = "air max"
    RUNNING = "running"
    TRAINING = "training"
    BASKETBALL = "basketball"
    FOOTBALL = "football"
    TENNIS = "tennis"
    GOLF = "golf"

class Gender(str, Enum):
    MEN = "men"
    WOMEN = "women"

class ShoppingRequest(BaseModel):
    shoe_type: ShoeType
    size: float
    gender: Gender
    budget: int | None = None
    color: str | None = None