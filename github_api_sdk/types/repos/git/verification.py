

from typing import Optional

from ...._models import BaseModel

__all__ = ["Verification"]


class Verification(BaseModel):
    payload: Optional[str] = None

    reason: str

    signature: Optional[str] = None

    verified: bool

    verified_at: Optional[str] = None
