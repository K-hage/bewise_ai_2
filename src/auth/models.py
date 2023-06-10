import uuid

from sqlalchemy import UUID, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String(100))
    access_token: Mapped[str] = mapped_column(
        String(200),
        unique=True,
        default=generate_uuid
    )
