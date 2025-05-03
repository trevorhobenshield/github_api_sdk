

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleFileExtensionRestriction", "Parameters"]


class Parameters(BaseModel):
    restricted_file_extensions: List[str]
    """The file extensions that are restricted from being pushed to the commit graph."""


class RepositoryRuleFileExtensionRestriction(BaseModel):
    type: Literal["file_extension_restriction"]

    parameters: Optional[Parameters] = None
