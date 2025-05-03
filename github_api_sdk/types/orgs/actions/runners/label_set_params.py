

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["LabelSetParams"]


class LabelSetParams(TypedDict, total=False):
    org: Required[str]

    labels: Required[list[str]]
    """The names of the custom labels to set for the runner.

    You can pass an empty array to remove all custom labels.
    """
