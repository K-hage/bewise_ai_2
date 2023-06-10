import uuid
from sqlalchemy import UUID, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Audio(Base):
    __tablename__ = 'audio'

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )
    user_id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id'))
    path: Mapped[str] = mapped_column(String(200))
