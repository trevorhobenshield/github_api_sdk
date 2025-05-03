

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..orgs.team import Team
from ..cvss_severity import CvssSeverity
from ..orgs.simple_user import SimpleUser
from ..security_advisory_ecosystem import SecurityAdvisoryEcosystem
from ..security_advisory_credit_type import SecurityAdvisoryCreditType
from .code_scanning.codeql.simple_repository import SimpleRepository

__all__ = [
    "RepositoryAdvisory",
    "Credit",
    "CreditsDetailed",
    "Cvss",
    "Cwe",
    "Identifier",
    "Submission",
    "Vulnerability",
    "VulnerabilityPackage",
]


class Credit(BaseModel):
    login: Optional[str] = None
    """The username of the user credited."""

    type: Optional[SecurityAdvisoryCreditType] = None
    """The type of credit the user is receiving."""


class CreditsDetailed(BaseModel):
    state: Literal["accepted", "declined", "pending"]
    """The state of the user's acceptance of the credit."""

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


class Submission(BaseModel):
    accepted: bool
    """
    Whether a private vulnerability report was accepted by the repository's
    administrators.
    """


class VulnerabilityPackage(BaseModel):
    ecosystem: SecurityAdvisoryEcosystem
    """The package's language or package management ecosystem."""

    name: Optional[str] = None
    """The unique package name within its ecosystem."""


class Vulnerability(BaseModel):
    package: Optional[VulnerabilityPackage] = None
    """The name of the package affected by the vulnerability."""

    patched_versions: Optional[str] = None
    """The package version(s) that resolve the vulnerability."""

    vulnerable_functions: Optional[List[str]] = None
    """The functions in the package that are affected."""

    vulnerable_version_range: Optional[str] = None
    """The range of the package versions affected by the vulnerability."""


class RepositoryAdvisory(BaseModel):
    author: Optional[SimpleUser] = None
    """A GitHub user."""

    closed_at: Optional[datetime] = None
    """The date and time of when the advisory was closed, in ISO 8601 format."""

    collaborating_teams: Optional[List[Team]] = None
    """A list of teams that collaborate on the advisory."""

    collaborating_users: Optional[List[SimpleUser]] = None
    """A list of users that collaborate on the advisory."""

    created_at: Optional[datetime] = None
    """The date and time of when the advisory was created, in ISO 8601 format."""

    credits: Optional[List[Credit]] = None

    credits_detailed: Optional[List[CreditsDetailed]] = None

    cve_id: Optional[str] = None
    """The Common Vulnerabilities and Exposures (CVE) ID."""

    cvss: Optional[Cvss] = None

    cwe_ids: Optional[List[str]] = None
    """A list of only the CWE IDs."""

    cwes: Optional[List[Cwe]] = None

    description: Optional[str] = None
    """A detailed description of what the advisory entails."""

    ghsa_id: str
    """The GitHub Security Advisory ID."""

    html_url: str
    """The URL for the advisory."""

    identifiers: List[Identifier]

    private_fork: Optional[SimpleRepository] = None
    """A GitHub repository."""

    published_at: Optional[datetime] = None
    """The date and time of when the advisory was published, in ISO 8601 format."""

    publisher: Optional[SimpleUser] = None
    """A GitHub user."""

    severity: Optional[Literal["critical", "high", "medium", "low"]] = None
    """The severity of the advisory."""

    state: Literal["published", "closed", "withdrawn", "draft", "triage"]
    """The state of the advisory."""

    submission: Optional[Submission] = None

    summary: str
    """A short summary of the advisory."""

    updated_at: Optional[datetime] = None
    """The date and time of when the advisory was last updated, in ISO 8601 format."""

    url: str
    """The API URL for the advisory."""

    vulnerabilities: Optional[List[Vulnerability]] = None

    withdrawn_at: Optional[datetime] = None
    """The date and time of when the advisory was withdrawn, in ISO 8601 format."""

    cvss_severities: Optional[CvssSeverity] = None
