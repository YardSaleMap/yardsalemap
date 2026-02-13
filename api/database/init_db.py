from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./test.db"

# Database engine setup
engine = create_engine(DATABASE_URL)

# SessionLocal for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Initialize database function
def init_database():
    # Create the database tables if they don't exist
    Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db() -> Session:
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield control to the caller
    finally:
        db.close()  # Close the session after use
