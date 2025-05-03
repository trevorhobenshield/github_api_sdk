

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleFilePathRestrictionParam", "Parameters"]


class Parameters(TypedDict, total=False):
    restricted_file_paths: Required[list[str]]
    """The file paths that are restricted from being pushed to the commit graph."""


class RepositoryRuleFilePathRestrictionParam(TypedDict, total=False):
    type: Required[Literal["file_path_restriction"]]

    parameters: Parameters
