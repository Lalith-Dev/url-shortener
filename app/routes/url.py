from fastapi import APIRouter
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
    
    url_db[short_code] = original_url
    
    return {
        "short_url": f"http://127.0.0.1:8000/{short_code}",
        "original_url": original_url
    }