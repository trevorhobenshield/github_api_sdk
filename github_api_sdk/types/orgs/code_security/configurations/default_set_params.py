

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DefaultSetParams"]


class DefaultSetParams(TypedDict, total=False):
    org: Required[str]

    default_for_new_repos: Literal["all", "none", "private_and_internal", "public"]
    """
    Specify which types of repository this security configuration should be applied
    to by default.
    """
