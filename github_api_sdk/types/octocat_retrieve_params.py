

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OctocatRetrieveParams"]


class OctocatRetrieveParams(TypedDict, total=False):
    s: str
    """The words to show in Octocat's speech bubble"""
