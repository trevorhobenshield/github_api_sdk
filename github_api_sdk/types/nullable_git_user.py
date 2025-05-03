

from typing import Optional

from .._models import BaseModel

__all__ = ["NullableGitUser"]


class NullableGitUser(BaseModel):
    date: Optional[str] = None

    email: Optional[str] = None

    name: Optional[str] = None
