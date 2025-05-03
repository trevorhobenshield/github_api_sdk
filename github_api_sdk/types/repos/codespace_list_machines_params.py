

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CodespaceListMachinesParams"]


class CodespaceListMachinesParams(TypedDict, total=False):
    owner: Required[str]

    client_ip: str
    """IP for location auto-detection when proxying a request"""

    location: str
    """The location to check for available machines. Assigned by IP if not provided."""

    ref: str
    """
    The branch or commit to check for prebuild availability and devcontainer
    restrictions.
    """
