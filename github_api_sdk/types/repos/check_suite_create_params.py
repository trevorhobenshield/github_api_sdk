

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CheckSuiteCreateParams"]


class CheckSuiteCreateParams(TypedDict, total=False):
    owner: Required[str]

    head_sha: Required[str]
    """The sha of the head commit."""
