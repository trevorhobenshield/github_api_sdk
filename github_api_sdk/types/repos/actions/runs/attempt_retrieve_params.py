

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AttemptRetrieveParams"]


class AttemptRetrieveParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    run_id: Required[int]

    exclude_pull_requests: bool
    """If `true` pull requests are omitted from the response (empty array)."""
