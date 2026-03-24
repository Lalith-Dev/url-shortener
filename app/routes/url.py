from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.schemas.url import URLRequest, URLResponse
from app.database.db import SessionLocal
from app.models.url import URL
import string
import random

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@router.post("/shorten", response_model=URLResponse)
def create_short_url(request: URLRequest, db: Session = Depends(get_db)):
    short_code = generate_short_code()

    # ensure unique
    while db.query(URL).filter(URL.short_code == short_code).first():
        short_code = generate_short_code()

    new_url = URL(
        short_code=short_code,
        original_url=request.original_url
    )

    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return {
        "short_url": f"http://127.0.0.1:8000/{short_code}",
        "original_url": request.original_url
    }

@router.get("/{short_code}")
def redirect_to_original_url(short_code: str, db: Session = Depends(get_db)):
    url_entry = db.query(URL).filter(URL.short_code == short_code).first()

    if not url_entry:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url=url_entry.original_url)