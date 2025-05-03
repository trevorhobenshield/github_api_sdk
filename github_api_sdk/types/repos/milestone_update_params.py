

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MilestoneUpdateParams"]


class MilestoneUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    description: str
    """A description of the milestone."""

    due_on: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """The milestone due date.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    state: Literal["open", "closed"]
    """The state of the milestone. Either `open` or `closed`."""

    title: str
    """The title of the milestone."""
