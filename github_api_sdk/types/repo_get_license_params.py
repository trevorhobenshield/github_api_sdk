

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RepoGetLicenseParams"]


class RepoGetLicenseParams(TypedDict, total=False):
    owner: Required[str]

    ref: str
    """The Git reference for the results you want to list.

    The `ref` for a branch can be formatted either as `refs/heads/<branch name>` or
    simply `<branch name>`. To reference a pull request use
    `refs/pull/<number>/merge`.
    """
