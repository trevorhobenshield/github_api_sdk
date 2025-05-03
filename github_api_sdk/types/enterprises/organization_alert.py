

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..applications.user import User
from ..repos.secret_scanning.alert_state import AlertState
from ..repos.secret_scanning.alert_resolution import AlertResolution
from ..repos.code_scanning.codeql.simple_repository import SimpleRepository

__all__ = ["OrganizationAlert"]


class OrganizationAlert(BaseModel):
    created_at: Optional[datetime] = None
    """The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."""

    html_url: Optional[str] = None
    """The GitHub URL of the alert resource."""

    is_base64_encoded: Optional[bool] = None
    """A boolean value representing whether or not alert is base64 encoded"""

    locations_url: Optional[str] = None
    """The REST API URL of the code locations for this alert."""

    multi_repo: Optional[bool] = None
    """
    Whether the detected secret was found in multiple repositories in the same
    organization or enterprise.
    """

    number: Optional[int] = None
    """The security alert number."""

    publicly_leaked: Optional[bool] = None
    """Whether the secret was publicly leaked."""

    push_protection_bypass_request_comment: Optional[str] = None
    """An optional comment when requesting a push protection bypass."""

    push_protection_bypass_request_html_url: Optional[str] = None
    """The URL to a push protection bypass request."""

    push_protection_bypass_request_reviewer: Optional[User] = None
    """A GitHub user."""

    push_protection_bypass_request_reviewer_comment: Optional[str] = None
    """An optional comment when reviewing a push protection bypass."""

    push_protection_bypassed: Optional[bool] = None
    """Whether push protection was bypassed for the detected secret."""

    push_protection_bypassed_at: Optional[datetime] = None
    """
    The time that push protection was bypassed in ISO 8601 format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """

    push_protection_bypassed_by: Optional[User] = None
    """A GitHub user."""

    repository: Optional[SimpleRepository] = None
    """A GitHub repository."""

    resolution: Optional[AlertResolution] = None
    """
    **Required when the `state` is `resolved`.** The reason for resolving the alert.
    """

    resolution_comment: Optional[str] = None
    """The comment that was optionally added when this alert was closed"""

    resolved_at: Optional[datetime] = None
    """
    The time that the alert was resolved in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    resolved_by: Optional[User] = None
    """A GitHub user."""

    secret: Optional[str] = None
    """The secret that was detected."""

    secret_type: Optional[str] = None
    """The type of secret that secret scanning detected."""

    secret_type_display_name: Optional[str] = None
    """
    User-friendly name for the detected secret, matching the `secret_type`. For a
    list of built-in patterns, see
    "[Supported secret scanning patterns](https://docs.github.com/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)."
    """

    state: Optional[AlertState] = None
    """Sets the state of the secret scanning alert.

    You must provide `resolution` when you set the state to `resolved`.
    """

    updated_at: Optional[datetime] = None
    """
    The time that the alert was last updated in ISO 8601 format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """

    url: Optional[str] = None
    """The REST API URL of the alert resource."""

    validity: Optional[Literal["active", "inactive", "unknown"]] = None
    """The token status as of the latest validity check."""
