from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    description: str


class ItemResponse(ItemCreate):
    id: int
    owner_id: int

    model_config = {"from_attributes": True}
