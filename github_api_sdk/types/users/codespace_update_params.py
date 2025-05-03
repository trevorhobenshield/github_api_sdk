

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["CodespaceUpdateParams"]


class CodespaceUpdateParams(TypedDict, total=False):
    display_name: str
    """Display name for this codespace"""

    machine: str
    """A valid machine to transition this codespace to."""

    recent_folders: list[str]
    """Recently opened folders inside the codespace.

    It is currently used by the clients to determine the folder path to load the
    codespace in.
    """
