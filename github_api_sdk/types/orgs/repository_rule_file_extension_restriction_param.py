

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleFileExtensionRestrictionParam", "Parameters"]


class Parameters(TypedDict, total=False):
    restricted_file_extensions: Required[list[str]]
    """The file extensions that are restricted from being pushed to the commit graph."""


class RepositoryRuleFileExtensionRestrictionParam(TypedDict, total=False):
    type: Required[Literal["file_extension_restriction"]]

    parameters: Parameters
