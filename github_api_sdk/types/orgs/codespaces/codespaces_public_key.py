

from typing import Optional

from ...._models import BaseModel

__all__ = ["CodespacesPublicKey"]


class CodespacesPublicKey(BaseModel):
    key: str
    """The Base64 encoded public key."""

    key_id: str
    """The identifier for the key."""

    id: Optional[int] = None

    created_at: Optional[str] = None

    title: Optional[str] = None

    url: Optional[str] = None
