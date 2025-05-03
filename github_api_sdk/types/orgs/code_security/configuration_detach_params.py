

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

__all__ = ["ConfigurationDetachParams"]


class ConfigurationDetachParams(TypedDict, total=False):
    selected_repository_ids: Iterable[int]
    """An array of repository IDs to detach from configurations."""
