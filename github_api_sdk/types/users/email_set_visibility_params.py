

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EmailSetVisibilityParams"]


class EmailSetVisibilityParams(TypedDict, total=False):
    visibility: Required[Literal["public", "private"]]
    """Denotes whether an email is publicly visible."""
