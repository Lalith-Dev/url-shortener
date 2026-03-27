from pydantic import BaseModel
from typing import Optional

class URLRequest(BaseModel):
    original_url: str
    expiry_seconds: Optional[int] = None 

class URLResponse(BaseModel):
    short_url: str
    original_url: str