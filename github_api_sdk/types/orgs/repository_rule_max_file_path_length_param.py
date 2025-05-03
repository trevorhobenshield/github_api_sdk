

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleMaxFilePathLengthParam", "Parameters"]


class Parameters(TypedDict, total=False):
    max_file_path_length: Required[int]
    """The maximum amount of characters allowed in file paths."""


class RepositoryRuleMaxFilePathLengthParam(TypedDict, total=False):
    type: Required[Literal["max_file_path_length"]]

    parameters: Parameters
