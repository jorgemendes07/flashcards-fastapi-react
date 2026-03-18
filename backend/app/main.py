from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.database import engine, Base, get_db
from app.models import User, Deck, Card
from app.schemas import UserCreate, UserResponse, DeckCreate, DeckResponse, CardCreate, CardResponse

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    pass

app = FastAPI(
    title="Flashcards App",
    lifespan=lifespan
)

# Users
@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    
    new_user = User(email=user.email, password=user.password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get("/users", response_model=List[UserResponse])
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

#Decks
@app.post("/decks", response_model=DeckResponse, status_code=201)
def create_deck(deck: DeckCreate, db: Session = Depends(get_db)):
    new_deck = Deck(name=deck.name, user_id=1)

    db.add(new_deck)
    db.commit()
    db.refresh(new_deck)
    return new_deck

@app.get("/decks", response_model=List[DeckResponse])
def list_decks(db: Session = Depends(get_db)):
    return db.query(Deck).all()

# Cards
@app.post("/cards", response_model=CardResponse, status_code=201)
def create_card(card: CardCreate, db: Session = Depends(get_db)):
    new_card = Card(front=card.front, back=card.back, difficulty=card.difficulty, deck_id=card.deck_id)

    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

@app.get("/{deck_id}/cards", response_model=List[CardResponse])
def list_cards(deck_id: int, db: Session = Depends(get_db)):
    deck = db.query(Deck).filter(Deck.id == deck_id).first()
    if not deck:
        raise HTTPException(status_code=404, detail="Deck não encontrado")

    return db.query(Card).filter(Card.deck_id == deck_id).all()