from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
import string
import random

router = APIRouter()

# temporary storage (in-memory)
url_db = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@router.post("/shorten")
def create_short_url(original_url: str):
    short_code = generate_short_code()

    while short_code in url_db:
        short_code = generate_short_code()

    url_db[short_code] = original_url

    return {
        "short_url": f"http://127.0.0.1:8000/{short_code}",
        "original_url": original_url
    }

@router.get("/{short_code}")
def redirect_to_original_url(short_code: str):
    original_url = url_db.get(short_code)

    if not original_url:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url=original_url)