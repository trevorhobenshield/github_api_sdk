

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleCreation"]


class RepositoryRuleCreation(BaseModel):
    type: Literal["creation"]
