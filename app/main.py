from fastapi import FastAPI
from app.routes import url
from app.database.db import engine, Base

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(url.router)

@app.get("/")
def home():
    return {"message": "URL Shortener API is running"}