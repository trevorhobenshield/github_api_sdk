

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReactionCreateParams"]


class ReactionCreateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    content: Required[Literal["+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"]]
    """
    The
    [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions)
    to add to the pull request review comment.
    """
