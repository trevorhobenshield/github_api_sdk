

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["RulesetVersion", "Actor"]


class Actor(BaseModel):
    id: Optional[int] = None

    type: Optional[str] = None


class RulesetVersion(BaseModel):
    actor: Actor
    """The actor who updated the ruleset"""

    updated_at: datetime

    version_id: int
    """The ID of the previous version of the ruleset"""
