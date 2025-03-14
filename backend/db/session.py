from contextlib import contextmanager
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.scoping import scoped_session
from typing import Any

from backend.db import base
from backend.db.exceptions import DatabaseError, MutationError

def get_session() -> scoped_session | None:
    return base.Session

@contextmanager
def session_commit(commit: bool = True) -> None:
    session = get_session()
    try:
        yield session
        if commit:
            session.commit()
    except SQLAlchemyError as sae:
        print(sae)
        session.rollback()
        raise DatabaseError() from sae
    except Exception as e:
        session.rollback()
        raise MutationError() from e
    """
    finally:
        session.close()
    """
