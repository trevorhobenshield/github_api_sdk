

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SecretScanningListAlertsParams"]


class SecretScanningListAlertsParams(TypedDict, total=False):
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

    is_multi_repo: bool
    """
    A boolean value representing whether or not to filter alerts by the multi-repo
    tag being present.
    """

    is_publicly_leaked: bool
    """
    A boolean value representing whether or not to filter alerts by the
    publicly-leaked tag being present.
    """

    per_page: int
    """The number of results per page (max 100).

    For more information, see
    "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."
    """

    resolution: str
    """A comma-separated list of resolutions.

    Only secret scanning alerts with one of these resolutions are listed. Valid
    resolutions are `false_positive`, `wont_fix`, `revoked`, `pattern_edited`,
    `pattern_deleted` or `used_in_tests`.
    """

    secret_type: str
    """A comma-separated list of secret types to return.

    All default secret patterns are returned. To return generic patterns, pass the
    token name(s) in the parameter. See
    "[Supported secret scanning patterns](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)"
    for a complete list of secret types.
    """

    sort: Literal["created", "updated"]
    """The property to sort the results by.

    `created` means when the alert was created. `updated` means when the alert was
    updated or resolved.
    """

    state: Literal["open", "resolved"]
    """
    Set to `open` or `resolved` to only list secret scanning alerts in a specific
    state.
    """

    validity: str
    """
    A comma-separated list of validities that, when present, will return alerts that
    match the validities in this list. Valid options are `active`, `inactive`, and
    `unknown`.
    """
