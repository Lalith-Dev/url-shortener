from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
import time

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = None

# 🔥 Retry connection
for i in range(10):
    try:
        engine = create_engine(DATABASE_URL)
        connection = engine.connect()
        connection.close()
        print("Connected to PostgreSQL ✅")
        break
    except Exception as e:
        print("Waiting for PostgreSQL...")
        time.sleep(2)

if engine is None:
    raise Exception("Could not connect to PostgreSQL")

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()