

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, TypedDict

from .security_advisory_ecosystem import SecurityAdvisoryEcosystem

__all__ = ["AdvisoryListParams"]


class AdvisoryListParams(TypedDict, total=False):
    affects: str | list[str]
    """
    If specified, only return advisories that affect any of `package` or
    `package@version`. A maximum of 1000 packages can be specified. If the query
    parameter causes the URL to exceed the maximum URL length supported by your
    client, you must specify fewer packages.

    Example: `affects=package1,package2@1.0.0,package3@^2.0.0` or
    `affects[]=package1&affects[]=package2@1.0.0`
    """

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

    cve_id: str
    """
    If specified, only advisories with this CVE (Common Vulnerabilities and
    Exposures) identifier will be returned.
    """

    cwes: str | list[str]
    """
    If specified, only advisories with these Common Weakness Enumerations (CWEs)
    will be returned.

    Example: `cwes=79,284,22` or `cwes[]=79&cwes[]=284&cwes[]=22`
    """

    direction: Literal["asc", "desc"]
    """The direction to sort the results by."""

    ecosystem: SecurityAdvisoryEcosystem
    """If specified, only advisories for these ecosystems will be returned."""

    epss_percentage: str
    """
    If specified, only return advisories that have an EPSS percentage score that
    matches the provided value. The EPSS percentage represents the likelihood of a
    CVE being exploited.
    """

    epss_percentile: str
    """
    If specified, only return advisories that have an EPSS percentile score that
    matches the provided value. The EPSS percentile represents the relative rank of
    the CVE's likelihood of being exploited compared to other CVEs.
    """

    ghsa_id: str
    """
    If specified, only advisories with this GHSA (GitHub Security Advisory)
    identifier will be returned.
    """

    is_withdrawn: bool
    """Whether to only return advisories that have been withdrawn."""

    modified: str
    """
    If specified, only show advisories that were updated or published on a date or
    date range.

    For more information on the syntax of the date range, see
    "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."
    """

    per_page: int
    """The number of results per page (max 100).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    published: str
    """
    If specified, only return advisories that were published on a date or date
    range.

    For more information on the syntax of the date range, see
    "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."
    """

    severity: Literal["unknown", "low", "medium", "high", "critical"]
    """If specified, only advisories with these severities will be returned."""

    sort: Literal["updated", "published", "epss_percentage", "epss_percentile"]
    """The property to sort the results by."""

    type: Literal["reviewed", "malware", "unreviewed"]
    """If specified, only advisories of this type will be returned.

    By default, a request with no other parameters defined will only return reviewed
    advisories that are not malware.
    """

    updated: str
    """If specified, only return advisories that were updated on a date or date range.

    For more information on the syntax of the date range, see
    "[Understanding the search syntax](https://docs.github.com/search-github/getting-started-with-searching-on-github/understanding-the-search-syntax#query-for-dates)."
    """
