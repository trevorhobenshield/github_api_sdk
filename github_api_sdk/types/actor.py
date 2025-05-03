

from typing import Optional

from .._models import BaseModel

__all__ = ["Actor"]


class Actor(BaseModel):
    id: int

    avatar_url: str

    gravatar_id: Optional[str] = None

    login: str

    url: str

    display_login: Optional[str] = None
