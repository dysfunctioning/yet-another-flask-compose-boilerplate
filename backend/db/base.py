import os

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase  # scoped_session, 
from sqlalchemy.orm.scoping import scoped_session
from backend.app.configuration import config
from backend.lib.logger import get_logger

logger = get_logger()

engine: Engine | None = None
Session: scoped_session | None = None

class Base(DeclarativeBase):
    pass


def initialize_database(database_url: str | None = None) -> None:
    global engine, Session
    database_url = database_url or os.environ['DATABASE_CONNECTION_URI']
    logger.info(f'Initializing Database with url: {database_url}')
    connection_args = {'connect_timeout': 10}
    engine = create_engine(database_url, echo=config.DEBUG_SQL, connect_args=connection_args)
    session_factory = sessionmaker(bind=engine)
    Session = scoped_session(session_factory)  # use scoped_session for thread safety



def get_engine() -> Engine | None:
    return engine
