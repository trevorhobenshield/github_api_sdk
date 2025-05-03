

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleMaxFilePathLength", "Parameters"]


class Parameters(BaseModel):
    max_file_path_length: int
    """The maximum amount of characters allowed in file paths."""


class RepositoryRuleMaxFilePathLength(BaseModel):
    type: Literal["max_file_path_length"]

    parameters: Optional[Parameters] = None
