from pydantic import BaseModel


class AudioResponse(BaseModel):
    download_url: str
