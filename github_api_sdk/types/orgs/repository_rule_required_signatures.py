

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleRequiredSignatures"]


class RepositoryRuleRequiredSignatures(BaseModel):
    type: Literal["required_signatures"]
