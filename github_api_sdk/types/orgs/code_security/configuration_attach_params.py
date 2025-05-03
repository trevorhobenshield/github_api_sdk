

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConfigurationAttachParams"]


class ConfigurationAttachParams(TypedDict, total=False):
    org: Required[str]

    scope: Required[Literal["all", "all_without_configurations", "public", "private_or_internal", "selected"]]
    """The type of repositories to attach the configuration to.

    `selected` means the configuration will be attached to only the repositories
    specified by `selected_repository_ids`
    """

    selected_repository_ids: Iterable[int]
    """An array of repository IDs to attach the configuration to.

    You can only provide a list of repository ids when the `scope` is set to
    `selected`.
    """
