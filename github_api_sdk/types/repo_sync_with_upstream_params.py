

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RepoSyncWithUpstreamParams"]


class RepoSyncWithUpstreamParams(TypedDict, total=False):
    owner: Required[str]

    branch: Required[str]
    """The name of the branch which should be updated to match upstream."""
