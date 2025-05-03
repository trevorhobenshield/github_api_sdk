

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleFilePathRestriction", "Parameters"]


class Parameters(BaseModel):
    restricted_file_paths: List[str]
    """The file paths that are restricted from being pushed to the commit graph."""


class RepositoryRuleFilePathRestriction(BaseModel):
    type: Literal["file_path_restriction"]

    parameters: Optional[Parameters] = None
