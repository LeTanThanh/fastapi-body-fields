from pydantic import BaseModel
from pydantic import Field

class Item(BaseModel):
  name: str = Field()
  description: str | None = Field(
    default = None,
    max_length = 300,
    description = "The description of the item"
  )
  price: float = Field(
    gt = 0,
    description = "The price must be greater than zero"
  )
  tax: float | None = Field(
    default = None
  )
