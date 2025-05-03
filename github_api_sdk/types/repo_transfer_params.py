

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RepoTransferParams"]


class RepoTransferParams(TypedDict, total=False):
    owner: Required[str]

    new_owner: Required[str]
    """The username or organization name the repository will be transferred to."""

    new_name: str
    """The new name to be given to the repository."""

    team_ids: Iterable[int]
    """ID of the team or teams to add to the repository.

    Teams can only be added to organization-owned repositories.
    """
