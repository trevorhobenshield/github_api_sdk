

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["LabelAddParams"]


class LabelAddParams(TypedDict, total=False):
    org: Required[str]

    labels: Required[list[str]]
    """The names of the custom labels to add to the runner."""
