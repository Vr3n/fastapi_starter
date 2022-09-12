"""
Database Settings and Configurations.

Creating Database Configution and Connecting the SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from api.settings.base import settings

## Database URL to Connect to SQL Alchemy.
## The url can be obtained from dashboard of your database.
SQL_ALCHEMY_DATABASE_URL = "postgresql://%s:%s@%s/%s" % (
    settings.POSTGRES_USER,
    settings.POSTGRES_PASSWORD,
    settings.POSTGRES_HOST,
    settings.POSTGRES_DB
)

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()