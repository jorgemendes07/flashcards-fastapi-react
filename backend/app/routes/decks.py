from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models import Deck, User
from app.database.database import get_db
from app.schemas.deck import DeckCreate, DeckUpdate, DeckResponse

router = APIRouter(prefix="/decks", tags=["Decks"])

@router.post("/user/{user_id}", response_model=DeckResponse, status_code=201)
def create_deck(user_id: int, deck: DeckCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    new_deck = Deck(name=deck.name, user_id=user_id)

    db.add(new_deck)
    db.commit()
    db.refresh(new_deck)
    return new_deck

@router.get("/user/{user_id}", response_model=List[DeckResponse])
def list_decks(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return db.query(Deck).filter(Deck.user_id == user_id).all()

@router.patch("/{deck_id}", response_model=DeckResponse)
def update_deck(deck_id: int, deck_data: DeckUpdate, db: Session = Depends(get_db)):
    db_deck = db.query(Deck).filter(Deck.id == deck_id).first()

    if not db_deck:
        raise HTTPException(status_code=404, detail="Deck não encontrado")
    
    db_deck.name = deck_data.name

    db.commit()
    db.refresh(db_deck)

    return db_deck

@router.delete("/{deck_id}", status_code=204)
def delete_deck(deck_id: int, db: Session = Depends(get_db)):
    db_deck = db.query(Deck).filter(Deck.id == deck_id).first()

    if not db_deck:
        raise HTTPException(status_code=404, detail="Deck não encontrado")
    
    db.delete(db_deck)
    db.commit()

    return None