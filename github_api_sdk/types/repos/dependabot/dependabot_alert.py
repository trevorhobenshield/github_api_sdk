

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...applications.user import User
from .dependabot_alert_package import DependabotAlertPackage
from .dependabot_alert_security_advisory import DependabotAlertSecurityAdvisory
from .dependabot_alert_security_vulnerability import DependabotAlertSecurityVulnerability

__all__ = ["DependabotAlert", "Dependency"]


class Dependency(BaseModel):
    manifest_path: Optional[str] = None
    """
    The full path to the dependency manifest file, relative to the root of the
    repository.
    """

    package: Optional[DependabotAlertPackage] = None
    """Details for the vulnerable package."""

    relationship: Optional[Literal["unknown", "direct", "transitive"]] = None
    """The vulnerable dependency's relationship to your project.

    > [!NOTE] We are rolling out support for dependency relationship across
    > ecosystems. This value will be "unknown" for all dependencies in unsupported
    > ecosystems.
    """

    scope: Optional[Literal["development", "runtime"]] = None
    """The execution scope of the vulnerable dependency."""


class DependabotAlert(BaseModel):
    created_at: datetime
    """The time that the alert was created in ISO 8601 format: `YYYY-MM-DDTHH:MM:SSZ`."""

    dependency: Dependency
    """Details for the vulnerable dependency."""

    dismissed_at: Optional[datetime] = None
    """
    The time that the alert was dismissed in ISO 8601 format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """

    dismissed_by: Optional[User] = None
    """A GitHub user."""

    dismissed_comment: Optional[str] = None
    """An optional comment associated with the alert's dismissal."""

    dismissed_reason: Optional[Literal["fix_started", "inaccurate", "no_bandwidth", "not_used", "tolerable_risk"]] = (
        None
    )
    """The reason that the alert was dismissed."""

    fixed_at: Optional[datetime] = None
    """
    The time that the alert was no longer detected and was considered fixed in ISO
    8601 format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    html_url: str
    """The GitHub URL of the alert resource."""

    number: int
    """The security alert number."""

    security_advisory: DependabotAlertSecurityAdvisory
    """Details for the GitHub Security Advisory."""

    security_vulnerability: DependabotAlertSecurityVulnerability
    """Details pertaining to one vulnerable version range for the advisory."""

    state: Literal["auto_dismissed", "dismissed", "fixed", "open"]
    """The state of the Dependabot alert."""

    updated_at: datetime
    """
    The time that the alert was last updated in ISO 8601 format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """

    url: str
    """The REST API URL of the alert resource."""

    auto_dismissed_at: Optional[datetime] = None
    """
    The time that the alert was auto-dismissed in ISO 8601 format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """
