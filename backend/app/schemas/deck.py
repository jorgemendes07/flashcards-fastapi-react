from pydantic import BaseModel, ConfigDict
from datetime import datetime

class DeckBase(BaseModel):
    name: str

class DeckCreate(DeckBase):
    pass

class DeckResponse(DeckBase):
    id: int
    user_id:int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)