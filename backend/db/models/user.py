from backend.db.base import Base

from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    # TODO: Determine BigIDs vs GUID:
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String())
    email: Mapped[str] = mapped_column(String())
    is_active: Mapped[bool] = mapped_column(default=True)


    def __repr__(self) -> str:
        return f'User(id={self.id}, email={self.email})'
