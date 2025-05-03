

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleRequiredLinearHistory"]


class RepositoryRuleRequiredLinearHistory(BaseModel):
    type: Literal["required_linear_history"]
