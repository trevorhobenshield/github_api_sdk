

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleDeletion"]


class RepositoryRuleDeletion(BaseModel):
    type: Literal["deletion"]
