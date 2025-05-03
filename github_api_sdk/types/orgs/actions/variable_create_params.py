

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VariableCreateParams"]


class VariableCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the variable."""

    value: Required[str]
    """The value of the variable."""

    visibility: Required[Literal["all", "private", "selected"]]
    """The type of repositories in the organization that can access the variable.

    `selected` means only the repositories specified by `selected_repository_ids`
    can access the variable.
    """

    selected_repository_ids: Iterable[int]
    """An array of repository ids that can access the organization variable.

    You can only provide a list of repository ids when the `visibility` is set to
    `selected`.
    """
