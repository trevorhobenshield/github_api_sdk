

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .cvss_severity import CvssSeverity
from .orgs.simple_user import SimpleUser
from .security_advisory_ecosystem import SecurityAdvisoryEcosystem
from .security_advisory_epp_score import SecurityAdvisoryEppScore
from .security_advisory_credit_type import SecurityAdvisoryCreditType

__all__ = ["GlobalAdvisory", "Credit", "Cvss", "Cwe", "Identifier", "Vulnerability", "VulnerabilityPackage"]


class Credit(BaseModel):
    type: SecurityAdvisoryCreditType
    """The type of credit the user is receiving."""

    user: SimpleUser
    """A GitHub user."""


class Cvss(BaseModel):
    score: Optional[float] = None
    """The CVSS score."""

    vector_string: Optional[str] = None
    """The CVSS vector."""


class Cwe(BaseModel):
    cwe_id: str
    """The Common Weakness Enumeration (CWE) identifier."""

    name: str
    """The name of the CWE."""


class Identifier(BaseModel):
    type: Literal["CVE", "GHSA"]
    """The type of identifier."""

    value: str
    """The identifier value."""


class VulnerabilityPackage(BaseModel):
    ecosystem: SecurityAdvisoryEcosystem
    """The package's language or package management ecosystem."""

    name: Optional[str] = None
    """The unique package name within its ecosystem."""


class Vulnerability(BaseModel):
    first_patched_version: Optional[str] = None
    """The package version that resolves the vulnerability."""

    package: Optional[VulnerabilityPackage] = None
    """The name of the package affected by the vulnerability."""

    vulnerable_functions: Optional[List[str]] = None
    """The functions in the package that are affected by the vulnerability."""

    vulnerable_version_range: Optional[str] = None
    """The range of the package versions affected by the vulnerability."""


class GlobalAdvisory(BaseModel):
    credits: Optional[List[Credit]] = None
    """The users who contributed to the advisory."""

    cve_id: Optional[str] = None
    """The Common Vulnerabilities and Exposures (CVE) ID."""

    cvss: Optional[Cvss] = None

    cwes: Optional[List[Cwe]] = None

    description: Optional[str] = None
    """A detailed description of what the advisory entails."""

    ghsa_id: str
    """The GitHub Security Advisory ID."""

    github_reviewed_at: Optional[datetime] = None
    """
    The date and time of when the advisory was reviewed by GitHub, in ISO 8601
    format.
    """

    html_url: str
    """The URL for the advisory."""

    identifiers: Optional[List[Identifier]] = None

    nvd_published_at: Optional[datetime] = None
    """
    The date and time when the advisory was published in the National Vulnerability
    Database, in ISO 8601 format. This field is only populated when the advisory is
    imported from the National Vulnerability Database.
    """

    published_at: datetime
    """The date and time of when the advisory was published, in ISO 8601 format."""

    references: Optional[List[str]] = None

    repository_advisory_url: Optional[str] = None
    """The API URL for the repository advisory."""

    severity: Literal["critical", "high", "medium", "low", "unknown"]
    """The severity of the advisory."""

    source_code_location: Optional[str] = None
    """The URL of the advisory's source code."""

    summary: str
    """A short summary of the advisory."""

    type: Literal["reviewed", "unreviewed", "malware"]
    """The type of advisory."""

    updated_at: datetime
    """The date and time of when the advisory was last updated, in ISO 8601 format."""

    url: str
    """The API URL for the advisory."""

    vulnerabilities: Optional[List[Vulnerability]] = None
    """The products and respective version ranges affected by the advisory."""

    withdrawn_at: Optional[datetime] = None
    """The date and time of when the advisory was withdrawn, in ISO 8601 format."""

    cvss_severities: Optional[CvssSeverity] = None

    epss: Optional[SecurityAdvisoryEppScore] = None
    """
    The EPSS scores as calculated by the
    [Exploit Prediction Scoring System](https://www.first.org/epss).
    """
