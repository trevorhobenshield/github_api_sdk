

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AppRemoveParams"]


class AppRemoveParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    apps: Required[list[str]]
    """The GitHub Apps that have push access to this branch.

    Use the slugified version of the app name. **Note**: The list of users, apps,
    and teams in total is limited to 100 items.
    """
