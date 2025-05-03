

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ConfigurationAttachParams"]


class ConfigurationAttachParams(TypedDict, total=False):
    enterprise: Required[str]

    scope: Required[Literal["all", "all_without_configurations"]]
    """The type of repositories to attach the configuration to."""
