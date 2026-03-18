from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

from app.models.card import CardDifficulty

class CardBase(BaseModel):
    front: str
    back: str
    difficulty: Optional[CardDifficulty] = None

class CardCreate(CardBase):
    deck_id: int

class CardResponse(CardBase):
    id: int
    deck_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)