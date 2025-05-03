

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CodeownerListErrorsParams"]


class CodeownerListErrorsParams(TypedDict, total=False):
    owner: Required[str]

    ref: str
    """
    A branch, tag or commit name used to determine which version of the CODEOWNERS
    file to use. Default: the repository's default branch (e.g. `main`)
    """
