import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Author, Post

# Create an in-memory SQLite database for testing
@pytest.fixture(scope='module')
def engine():
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)
    return engine

@pytest.fixture(scope='module')
def Session(engine):
    return sessionmaker(bind=engine)

@pytest.fixture(scope='function')
def session(Session):
    session = Session()
    yield session
    session.rollback()
    session.close()

