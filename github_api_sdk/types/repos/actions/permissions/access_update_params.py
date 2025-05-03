

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccessUpdateParams"]


class AccessUpdateParams(TypedDict, total=False):
    owner: Required[str]

    access_level: Required[Literal["none", "user", "organization"]]
    """
    Defines the level of access that workflows outside of the repository have to
    actions and reusable workflows within the repository.

    `none` means the access is only possible from workflows in this repository.
    `user` level access allows sharing across user owned private repositories only.
    `organization` level access allows sharing across the organization.
    """
