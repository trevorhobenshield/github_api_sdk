

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["ScanningOptionsParam"]


class ScanningOptionsParam(TypedDict, total=False):
    runner_label: str | None
    """
    The label of the runner to use for code scanning default setup when runner_type
    is 'labeled'.
    """

    runner_type: Literal["standard", "labeled", "not_set"]
    """Whether to use labeled runners or standard GitHub runners."""
