

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CodespaceGetDefaultAttributesParams"]


class CodespaceGetDefaultAttributesParams(TypedDict, total=False):
    owner: Required[str]

    client_ip: str
    """
    An alternative IP for default location auto-detection, such as when proxying a
    request.
    """

    ref: str
    """The branch or commit to check for a default devcontainer path.

    If not specified, the default branch will be checked.
    """
