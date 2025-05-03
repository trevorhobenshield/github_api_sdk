

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImportUpdateParams"]


class ImportUpdateParams(TypedDict, total=False):
    owner: Required[str]

    tfvc_project: str
    """For a tfvc import, the name of the project that is being imported."""

    vcs: Literal["subversion", "tfvc", "git", "mercurial"]
    """The type of version control system you are migrating from."""

    vcs_password: str
    """The password to provide to the originating repository."""

    vcs_username: str
    """The username to provide to the originating repository."""
