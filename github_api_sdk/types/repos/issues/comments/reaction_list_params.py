

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReactionListParams"]


class ReactionListParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    content: Literal["+1", "-1", "laugh", "confused", "heart", "hooray", "rocket", "eyes"]
    """
    Returns a single
    [reaction type](https://docs.github.com/rest/reactions/reactions#about-reactions).
    Omit this parameter to list all reactions to an issue comment.
    """

    page: int
    """The page number of the results to fetch.

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    per_page: int
    """The number of results per page (max 100).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """
