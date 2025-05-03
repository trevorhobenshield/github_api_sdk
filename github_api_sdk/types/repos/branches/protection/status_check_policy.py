

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["StatusCheckPolicy", "Check"]


class Check(BaseModel):
    app_id: Optional[int] = None

    context: str


class StatusCheckPolicy(BaseModel):
    checks: List[Check]

    contexts: List[str]

    contexts_url: str

    strict: bool

    url: str
