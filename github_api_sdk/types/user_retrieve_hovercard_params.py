

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["UserRetrieveHovercardParams"]


class UserRetrieveHovercardParams(TypedDict, total=False):
    subject_id: str
    """Uses the ID for the `subject_type` you specified.

    **Required** when using `subject_type`.
    """

    subject_type: Literal["organization", "repository", "issue", "pull_request"]
    """
    Identifies which additional information you'd like to receive about the person's
    hovercard. Can be `organization`, `repository`, `issue`, `pull_request`.
    **Required** when using `subject_id`.
    """
