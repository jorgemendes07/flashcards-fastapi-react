from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database.database import engine, Base
import app.models

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield
    pass

app = FastAPI(
    title="Flashcards App",
    lifespan=lifespan
)


@app.get("/")
def read_root():
    return {"Message": "Flashcards App"}
