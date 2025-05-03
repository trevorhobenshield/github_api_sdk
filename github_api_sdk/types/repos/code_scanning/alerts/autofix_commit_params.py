

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AutofixCommitParams"]


class AutofixCommitParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    message: str
    """Commit message to be used."""

    target_ref: str
    """The Git reference of target branch for the commit.

    Branch needs to already exist. For more information, see
    "[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)"
    in the Git documentation.
    """
