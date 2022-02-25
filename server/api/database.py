from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

with open("/run/secrets/db-password") as f:
    password = f.read().strip()

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://postgres:{password}@db/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
