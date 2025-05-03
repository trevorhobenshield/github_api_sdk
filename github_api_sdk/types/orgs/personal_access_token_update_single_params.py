

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PersonalAccessTokenUpdateSingleParams"]


class PersonalAccessTokenUpdateSingleParams(TypedDict, total=False):
    org: Required[str]

    action: Required[Literal["revoke"]]
    """Action to apply to the fine-grained personal access token."""
