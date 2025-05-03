

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["VariableUpdateParams"]


class VariableUpdateParams(TypedDict, total=False):
    org: Required[str]

    body_name: Annotated[str, PropertyInfo(alias="name")]
    """The name of the variable."""

    selected_repository_ids: Iterable[int]
    """An array of repository ids that can access the organization variable.

    You can only provide a list of repository ids when the `visibility` is set to
    `selected`.
    """

    value: str
    """The value of the variable."""

    visibility: Literal["all", "private", "selected"]
    """The type of repositories in the organization that can access the variable.

    `selected` means only the repositories specified by `selected_repository_ids`
    can access the variable.
    """
