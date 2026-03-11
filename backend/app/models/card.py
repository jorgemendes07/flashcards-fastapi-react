from datetime import datetime
from typing import TYPE_CHECKING, Optional
import enum

from sqlalchemy import String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database import Base

class CardDifficulty(enum.Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

if TYPE_CHECKING:
    from .user import User
    from .deck import Deck

class Card(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    deck_id: Mapped[int] = mapped_column(ForeignKey("decks.id"), nullable=False)

    front: Mapped[str ]= mapped_column(String(255), index=True, nullable=False)
    back: Mapped[str] = mapped_column(String(255), nullable=False)
    difficulty: Mapped[Optional[CardDifficulty]] = mapped_column(nullable=True)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now()) 
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    deck: Mapped["Deck"] = relationship(back_populates="cards")