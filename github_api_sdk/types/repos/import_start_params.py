

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImportStartParams"]


class ImportStartParams(TypedDict, total=False):
    owner: Required[str]

    vcs_url: Required[str]
    """The URL of the originating repository."""

    tfvc_project: str
    """For a tfvc import, the name of the project that is being imported."""

    vcs: Literal["subversion", "git", "mercurial", "tfvc"]
    """The originating VCS type.

    Without this parameter, the import job will take additional time to detect the
    VCS type before beginning the import. This detection step will be reflected in
    the response.
    """

    vcs_password: str
    """If authentication is required, the password to provide to `vcs_url`."""

    vcs_username: str
    """If authentication is required, the username to provide to `vcs_url`."""
