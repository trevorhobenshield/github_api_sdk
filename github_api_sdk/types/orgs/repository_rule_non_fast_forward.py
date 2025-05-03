

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleNonFastForward"]


class RepositoryRuleNonFastForward(BaseModel):
    type: Literal["non_fast_forward"]
