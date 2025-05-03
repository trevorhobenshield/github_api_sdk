

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MilestoneCreateParams"]


class MilestoneCreateParams(TypedDict, total=False):
    owner: Required[str]

    title: Required[str]
    """The title of the milestone."""

    description: str
    """A description of the milestone."""

    due_on: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """The milestone due date.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    state: Literal["open", "closed"]
    """The state of the milestone. Either `open` or `closed`."""
