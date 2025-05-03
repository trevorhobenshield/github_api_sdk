

from typing import Optional

from ..._models import BaseModel

__all__ = ["AttestationCreateResponse"]


class AttestationCreateResponse(BaseModel):
    id: Optional[int] = None
    """The ID of the attestation."""
