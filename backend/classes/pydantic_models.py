from pydantic import BaseModel

class ShoppingRequest(BaseModel):
    shoe_type: str
    size: float
    budget: int | None = None
    color: str | None = None