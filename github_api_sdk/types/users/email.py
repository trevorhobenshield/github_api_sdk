

from typing import Optional

from ..._models import BaseModel

__all__ = ["Email"]


class Email(BaseModel):
    email: str

    primary: bool

    verified: bool

    visibility: Optional[str] = None
