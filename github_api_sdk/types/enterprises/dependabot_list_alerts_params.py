

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DependabotListAlertsParams"]


class DependabotListAlertsParams(TypedDict, total=False):
    after: str
    """
    A cursor, as given in the
    [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
    If specified, the query only searches for results after this cursor. For more
    information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    before: str
    """
    A cursor, as given in the
    [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
    If specified, the query only searches for results before this cursor. For more
    information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    direction: Literal["asc", "desc"]
    """The direction to sort the results by."""

    ecosystem: str
    """A comma-separated list of ecosystems.

    If specified, only alerts for these ecosystems will be returned.

    Can be: `composer`, `go`, `maven`, `npm`, `nuget`, `pip`, `pub`, `rubygems`,
    `rust`
    """

    epss_percentage: str
    """CVE Exploit Prediction Scoring System (EPSS) percentage. Can be specified as:

    - An exact number (`n`)
    - Comparators such as `>n`, `<n`, `>=n`, `<=n`
    - A range like `n..n`, where `n` is a number from 0.0 to 1.0

    Filters the list of alerts based on EPSS percentages. If specified, only alerts
    with the provided EPSS percentages will be returned.
    """

    first: int
    """**Deprecated**.

    The number of results per page (max 100), starting from the first matching
    result. This parameter must not be used in combination with `last`. Instead, use
    `per_page` in combination with `after` to fetch the first page of results.
    """

    last: int
    """**Deprecated**.

    The number of results per page (max 100), starting from the last matching
    result. This parameter must not be used in combination with `first`. Instead,
    use `per_page` in combination with `before` to fetch the last page of results.
    """

    package: str
    """A comma-separated list of package names.

    If specified, only alerts for these packages will be returned.
    """

    per_page: int
    """The number of results per page (max 100).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    scope: Literal["development", "runtime"]
    """The scope of the vulnerable dependency.

    If specified, only alerts with this scope will be returned.
    """

    severity: str
    """A comma-separated list of severities.

    If specified, only alerts with these severities will be returned.

    Can be: `low`, `medium`, `high`, `critical`
    """

    sort: Literal["created", "updated", "epss_percentage"]
    """
    The property by which to sort the results. `created` means when the alert was
    created. `updated` means when the alert's state last changed. `epss_percentage`
    sorts alerts by the Exploit Prediction Scoring System (EPSS) percentage.
    """

    state: str
    """A comma-separated list of states.

    If specified, only alerts with these states will be returned.

    Can be: `auto_dismissed`, `dismissed`, `fixed`, `open`
    """
