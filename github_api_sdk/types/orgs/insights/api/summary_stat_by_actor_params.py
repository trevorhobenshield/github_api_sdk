

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SummaryStatByActorParams"]


class SummaryStatByActorParams(TypedDict, total=False):
    org: Required[str]

    actor_type: Required[
        Literal["installation", "classic_pat", "fine_grained_pat", "oauth_app", "github_app_user_to_server"]
    ]

    min_timestamp: Required[str]
    """The minimum timestamp to query for stats.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    max_timestamp: str
    """The maximum timestamp to query for stats.

    Defaults to the time 30 days ago. This is a timestamp in
    [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """
