

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TreeRetrieveParams"]


class TreeRetrieveParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    recursive: str
    """
    Setting this parameter to any value returns the objects or subtrees referenced
    by the tree specified in `:tree_sha`. For example, setting `recursive` to any of
    the following will enable returning objects or subtrees: `0`, `1`, `"true"`, and
    `"false"`. Omit this parameter to prevent recursively returning objects or
    subtrees.
    """
