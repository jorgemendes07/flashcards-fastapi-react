from fastapi import FastAPI
from app.routes import users, decks, cards
from app.database.database import engine, Base

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    pass

app = FastAPI(
    title="Flashcards App",
    lifespan=lifespan
)

# rotas
app.include_router(cards.router)
app.include_router(decks.router)
app.include_router(users.router)