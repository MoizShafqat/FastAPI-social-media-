from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:allah@123 @localhost:5432/fastapi"
from urllib.parse import quote_plus

password = quote_plus("allah@123")  # handles spaces, @, etc.
SQLALCHEMY_DATABASE_URL  = f"postgresql://postgres:{password}@localhost:5432/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
