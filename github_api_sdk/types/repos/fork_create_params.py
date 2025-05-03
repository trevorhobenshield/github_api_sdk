

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ForkCreateParams"]


class ForkCreateParams(TypedDict, total=False):
    owner: Required[str]

    default_branch_only: bool
    """When forking from an existing repository, fork with only the default branch."""

    name: str
    """When forking from an existing repository, a new name for the fork."""

    organization: str
    """
    Optional parameter to specify the organization name if forking into an
    organization.
    """
