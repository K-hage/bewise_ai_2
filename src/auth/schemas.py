from uuid import UUID

from pydantic import BaseModel, Field


class UserCreateRequest(BaseModel):
    name: str = Field(min_length=3)


class UserCreateResponse(BaseModel):
    id: UUID
    access_token: str

    @classmethod
    def from_orm(cls, user):
        return cls(
            id=user.id,
            access_token=user.access_token,
        )
