

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrafficGetClonesParams"]


class TrafficGetClonesParams(TypedDict, total=False):
    owner: Required[str]

    per: Literal["day", "week"]
    """The time frame to display results for."""
