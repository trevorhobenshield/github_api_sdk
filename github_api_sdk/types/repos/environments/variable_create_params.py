

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VariableCreateParams"]


class VariableCreateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    name: Required[str]
    """The name of the variable."""

    value: Required[str]
    """The value of the variable."""
