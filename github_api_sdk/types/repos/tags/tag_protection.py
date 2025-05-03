

from typing import Optional

from ...._models import BaseModel

__all__ = ["TagProtection"]


class TagProtection(BaseModel):
    pattern: str

    id: Optional[int] = None

    created_at: Optional[str] = None

    enabled: Optional[bool] = None

    updated_at: Optional[str] = None
