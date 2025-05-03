

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RunnerSetParams"]


class RunnerSetParams(TypedDict, total=False):
    org: Required[str]

    runners: Required[Iterable[int]]
    """List of runner IDs to add to the runner group."""
