from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timedelta
from app.database.db import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String, unique=True, index=True)
    original_url = Column(String)
    expiry_time = Column(DateTime, nullable=True)
    clicks = Column(Integer, default=0)  # 👈 NEW