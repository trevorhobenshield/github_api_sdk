

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["KeyCreateParams"]


class KeyCreateParams(TypedDict, total=False):
    owner: Required[str]

    key: Required[str]
    """The contents of the key."""

    read_only: bool
    """If `true`, the key will only be able to read repository contents.

    Otherwise, the key will be able to read and write.

    Deploy keys with write access can perform the same actions as an organization
    member with admin access, or a collaborator on a personal repository. For more
    information, see
    "[Repository permission levels for an organization](https://docs.github.com/articles/repository-permission-levels-for-an-organization/)"
    and
    "[Permission levels for a user account repository](https://docs.github.com/articles/permission-levels-for-a-user-account-repository/)."
    """

    title: str
    """A name for the key."""
