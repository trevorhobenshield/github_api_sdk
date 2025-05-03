

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleMaxFileSizeParam", "Parameters"]


class Parameters(TypedDict, total=False):
    max_file_size: Required[int]
    """The maximum file size allowed in megabytes.

    This limit does not apply to Git Large File Storage (Git LFS).
    """


class RepositoryRuleMaxFileSizeParam(TypedDict, total=False):
    type: Required[Literal["max_file_size"]]

    parameters: Parameters
