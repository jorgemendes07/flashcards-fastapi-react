from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models import Card, Deck
from app.database.database import get_db
from app.schemas.card import CardCreate, CardResponse, CardUpdate

router = APIRouter(prefix="/cards", tags=["Cards"])

@router.post("/deck/{deck_id}", response_model=CardResponse, status_code=201)
def create_card(deck_id: int, card: CardCreate, db: Session = Depends(get_db)):
    deck = db.query(Deck).filter(Deck.id == deck_id).first()
    
    if not deck:
        raise HTTPException(status_code=404, detail="Deck não encontrado")
     
    new_card = Card(front=card.front, back=card.back, difficulty=card.difficulty, deck_id=deck_id)

    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

@router.get("/deck/{deck_id}", response_model=List[CardResponse])
def list_cards(deck_id: int, db: Session = Depends(get_db)):
    deck = db.query(Deck).filter(Deck.id == deck_id).first()
    
    if not deck:
        raise HTTPException(status_code=404, detail="Deck não encontrado")

    return db.query(Card).filter(Card.deck_id == deck_id).all()

@router.patch("/{card_id}", response_model=CardResponse)
def update_card(card_id: int, card_data: CardUpdate, db: Session = Depends(get_db)):
    db_card = db.query(Card).filter(Card.id == card_id).first()

    if not db_card:
        raise HTTPException(status_code=404, detail="Card não encontrado")
    
    update_data = card_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_card, key, value)

    db.commit()
    db.refresh(db_card)

    return db_card

@router.delete("/{card_id}", status_code=204)
def delete_card(card_id: int, db: Session = Depends(get_db)):
    db_card = db.query(Card).filter(Card.id == card_id).first()

    if not db_card:
        raise HTTPException(status_code=404, detail="Card não encontrado")
    
    db.delete(db_card)
    db.commit()

    return None