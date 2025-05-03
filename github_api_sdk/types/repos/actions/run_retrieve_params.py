

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RunRetrieveParams"]


class RunRetrieveParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    exclude_pull_requests: bool
    """If `true` pull requests are omitted from the response (empty array)."""
