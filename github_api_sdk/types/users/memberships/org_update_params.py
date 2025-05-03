

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrgUpdateParams"]


class OrgUpdateParams(TypedDict, total=False):
    state: Required[Literal["active"]]
    """The state that the membership should be in. Only `"active"` will be accepted."""
