

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VariableUpdateParams"]


class VariableUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    body_name: Annotated[str, PropertyInfo(alias="name")]
    """The name of the variable."""

    value: str
    """The value of the variable."""
