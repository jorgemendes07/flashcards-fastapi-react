from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import engine, Base, get_db
from app.models import User, Deck, Card
from app.schemas import UserCreate,UserUpdate, UserResponse, DeckCreate, DeckUpdate, DeckResponse, CardCreate, CardUpdate, CardResponse

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

@app.patch("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    if user_data.email:
        email_exists = db.query(User).filter(
            User.email == user_data.email,
            User.id != user_id
        ).first()
    
        if email_exists:
            raise HTTPException(status_code=400, detail="E-mail já está em uso")
    
        db_user.email = user_data.email

    if user_data.password:
        db_user.password = user_data.password

    db.commit()
    db.refresh(db_user)
    return db_user

#Decks
@app.post("/{user_id}/decks", response_model=DeckResponse, status_code=201)
def create_deck(user_id: int, deck: DeckCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    new_deck = Deck(name=deck.name, user_id=user_id)

    db.add(new_deck)
    db.commit()
    db.refresh(new_deck)
    return new_deck

@app.get("/{user_id}/decks", response_model=List[DeckResponse])
def list_decks(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return db.query(Deck).filter(Deck.user_id == user_id).all()

@app.patch("/decks/{deck_id}", response_model=DeckResponse)
def update_deck(deck_id: int, deck_data: DeckUpdate, db: Session = Depends(get_db)):
    db_deck = db.query(Deck).filter(Deck.id == deck_id).first()

    if not db_deck:
        raise HTTPException(status_code=404, detail="Deck não encontrado")
    
    db_deck.name = deck_data.name

    db.commit()
    db.refresh(db_deck)

    return db_deck

@app.delete("/decks/{deck_id}", status_code=204)
def delete_deck(deck_id: int, db: Session = Depends(get_db)):
    db_deck = db.query(Deck).filter(Deck.id == deck_id).first()

    if not db_deck:
        raise HTTPException(status_code=404, detail="Deck não encontrado")
    
    db.delete(db_deck)
    db.commit()

    return None

# Cards
@app.post("/{user_id}/{deck_id}/cards", response_model=CardResponse, status_code=201)
def create_card(user_id: int, deck_id: int, card: CardCreate, db: Session = Depends(get_db)):
    deck = db.query(Deck).filter(Deck.id == deck_id, Deck.user_id == user_id).first()
    
    if not deck:
        raise HTTPException(status_code=404, detail="Deck não encontrado")
     
    new_card = Card(front=card.front, back=card.back, difficulty=card.difficulty, deck_id=deck_id)

    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

@app.get("/{user_id}/{deck_id}/cards", response_model=List[CardResponse])
def list_cards(user_id: int, deck_id: int, db: Session = Depends(get_db)):
    deck = db.query(Deck).filter(Deck.id == deck_id, Deck.user_id == user_id).first()
    
    if not deck:
        raise HTTPException(status_code=404, detail="Deck não encontrado")

    return db.query(Card).filter(Card.deck_id == deck_id).all()

@app.patch("/cards/{card_id}", response_model=CardResponse)
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

@app.delete("/cards/{card_id}", status_code=204)
def delete_card(card_id: int, db: Session = Depends(get_db)):
    db_card = db.query(Card).filter(Card.id == card_id).first()

    if not db_card:
        raise HTTPException(status_code=404, detail="Card não encontrado")
    
    db.delete(db_card)
    db.commit()

    return None