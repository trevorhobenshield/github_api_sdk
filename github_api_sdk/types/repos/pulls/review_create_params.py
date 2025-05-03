

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReviewCreateParams", "Comment"]


class ReviewCreateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    body: str
    """**Required** when using `REQUEST_CHANGES` or `COMMENT` for the `event`
    parameter.

    The body text of the pull request review.
    """

    comments: Iterable[Comment]
    """
    Use the following table to specify the location, destination, and contents of
    the draft review comment.
    """

    commit_id: str
    """The SHA of the commit that needs a review.

    Not using the latest commit SHA may render your review comment outdated if a
    subsequent commit modifies the line you specify as the `position`. Defaults to
    the most recent commit in the pull request when you do not specify a value.
    """

    event: Literal["APPROVE", "REQUEST_CHANGES", "COMMENT"]
    """The review action you want to perform.

    The review actions include: `APPROVE`, `REQUEST_CHANGES`, or `COMMENT`. By
    leaving this blank, you set the review action state to `PENDING`, which means
    you will need to
    [submit the pull request review](https://docs.github.com/rest/pulls/reviews#submit-a-review-for-a-pull-request)
    when you are ready.
    """


class Comment(TypedDict, total=False):
    body: Required[str]
    """Text of the review comment."""

    path: Required[str]
    """The relative path to the file that necessitates a review comment."""

    line: int

    position: int
    """The position in the diff where you want to add a review comment.

    Note this value is not the same as the line number in the file. The `position`
    value equals the number of lines down from the first "@@" hunk header in the
    file you want to add a comment. The line just below the "@@" line is position 1,
    the next line is position 2, and so on. The position in the diff continues to
    increase through lines of whitespace and additional hunks until the beginning of
    a new file.
    """

    side: str

    start_line: int

    start_side: str
