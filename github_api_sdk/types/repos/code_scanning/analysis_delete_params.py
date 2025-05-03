

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["AnalysisDeleteParams"]


class AnalysisDeleteParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    confirm_delete: str | None
    """Allow deletion if the specified analysis is the last in a set.

    If you attempt to delete the final analysis in a set without setting this
    parameter to `true`, you'll get a 400 response with the message:
    `Analysis is last of its type and deletion may result in the loss of historical alert data. Please specify confirm_delete.`
    """
