

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleUpdate", "Parameters"]


class Parameters(BaseModel):
    update_allows_fetch_and_merge: bool
    """Branch can pull changes from its upstream repository"""


class RepositoryRuleUpdate(BaseModel):
    type: Literal["update"]

    parameters: Optional[Parameters] = None
