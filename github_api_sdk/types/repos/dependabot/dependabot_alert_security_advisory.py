

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...cvss_severity import CvssSeverity
from ...security_advisory_epp_score import SecurityAdvisoryEppScore
from .dependabot_alert_security_vulnerability import DependabotAlertSecurityVulnerability

__all__ = ["DependabotAlertSecurityAdvisory", "Cvss", "Cwe", "Identifier", "Reference"]


class Cvss(BaseModel):
    score: float
    """The overall CVSS score of the advisory."""

    vector_string: Optional[str] = None
    """The full CVSS vector string for the advisory."""


class Cwe(BaseModel):
    cwe_id: str
    """The unique CWE ID."""

    name: str
    """The short, plain text name of the CWE."""


class Identifier(BaseModel):
    type: Literal["CVE", "GHSA"]
    """The type of advisory identifier."""

    value: str
    """The value of the advisory identifer."""


class Reference(BaseModel):
    url: str
    """The URL of the reference."""


class DependabotAlertSecurityAdvisory(BaseModel):
    cve_id: Optional[str] = None
    """The unique CVE ID assigned to the advisory."""

    cvss: Cvss
    """Details for the advisory pertaining to the Common Vulnerability Scoring System."""

    cwes: List[Cwe]
    """Details for the advisory pertaining to Common Weakness Enumeration."""

    description: str
    """A long-form Markdown-supported description of the advisory."""

    ghsa_id: str
    """The unique GitHub Security Advisory ID assigned to the advisory."""

    identifiers: List[Identifier]
    """Values that identify this advisory among security information sources."""

    published_at: datetime
    """
    The time that the advisory was published in ISO 8601 format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """

    references: List[Reference]
    """Links to additional advisory information."""

    severity: Literal["low", "medium", "high", "critical"]
    """The severity of the advisory."""

    summary: str
    """A short, plain text summary of the advisory."""

    updated_at: datetime
    """
    The time that the advisory was last modified in ISO 8601 format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """

    vulnerabilities: List[DependabotAlertSecurityVulnerability]
    """Vulnerable version range information for the advisory."""

    withdrawn_at: Optional[datetime] = None
    """
    The time that the advisory was withdrawn in ISO 8601 format:
    `YYYY-MM-DDTHH:MM:SSZ`.
    """

    cvss_severities: Optional[CvssSeverity] = None

    epss: Optional[SecurityAdvisoryEppScore] = None
    """
    The EPSS scores as calculated by the
    [Exploit Prediction Scoring System](https://www.first.org/epss).
    """
