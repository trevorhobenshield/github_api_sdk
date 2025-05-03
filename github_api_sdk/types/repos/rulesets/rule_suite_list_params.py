

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleSuiteListParams"]


class RuleSuiteListParams(TypedDict, total=False):
    owner: Required[str]

    actor_name: str
    """The handle for the GitHub user account to filter on.

    When specified, only rule evaluations triggered by this actor will be returned.
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

    ref: str
    """The name of the ref.

    Cannot contain wildcard characters. Optionally prefix with `refs/heads/` to
    limit to branches or `refs/tags/` to limit to tags. Omit the prefix to search
    across all refs. When specified, only rule evaluations triggered for this ref
    will be returned.
    """

    rule_suite_result: Literal["pass", "fail", "bypass", "all"]
    """The rule results to filter on.

    When specified, only suites with this result will be returned.
    """

    time_period: Literal["hour", "day", "week", "month"]
    """The time period to filter by.

    For example, `day` will filter for rule suites that occurred in the past 24
    hours, and `week` will filter for insights that occurred in the past 7 days (168
    hours).
    """
