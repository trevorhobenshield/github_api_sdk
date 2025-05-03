

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["TopicReplaceParams"]


class TopicReplaceParams(TypedDict, total=False):
    owner: Required[str]

    names: Required[list[str]]
    """An array of topics to add to the repository.

    Pass one or more topics to _replace_ the set of existing topics. Send an empty
    array (`[]`) to clear all topics from the repository. **Note:** Topic `names`
    will be saved as lowercase.
    """
