from pydantic import BaseModel
from backend.classes.state import Gender

class ShoppingRequest(BaseModel):
    shoe_type: str
    size: float
    gender: Gender
    budget: int | None = None
    color: str | None = None