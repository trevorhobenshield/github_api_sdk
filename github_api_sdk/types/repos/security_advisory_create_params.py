

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..security_advisory_ecosystem import SecurityAdvisoryEcosystem
from ..security_advisory_credit_type import SecurityAdvisoryCreditType

__all__ = ["SecurityAdvisoryCreateParams", "Vulnerability", "VulnerabilityPackage", "Credit"]


class SecurityAdvisoryCreateParams(TypedDict, total=False):
    owner: Required[str]

    description: Required[str]
    """A detailed description of what the advisory impacts."""

    summary: Required[str]
    """A short summary of the advisory."""

    vulnerabilities: Required[Iterable[Vulnerability]]
    """
    A product affected by the vulnerability detailed in a repository security
    advisory.
    """

    credits: Iterable[Credit] | None
    """
    A list of users receiving credit for their participation in the security
    advisory.
    """

    cve_id: str | None
    """The Common Vulnerabilities and Exposures (CVE) ID."""

    cvss_vector_string: str | None
    """The CVSS vector that calculates the severity of the advisory.

    You must choose between setting this field or `severity`.
    """

    cwe_ids: list[str] | None
    """A list of Common Weakness Enumeration (CWE) IDs."""

    severity: Literal["critical", "high", "medium", "low"] | None
    """The severity of the advisory.

    You must choose between setting this field or `cvss_vector_string`.
    """

    start_private_fork: bool
    """
    Whether to create a temporary private fork of the repository to collaborate on a
    fix.
    """


class VulnerabilityPackage(TypedDict, total=False):
    ecosystem: Required[SecurityAdvisoryEcosystem]
    """The package's language or package management ecosystem."""

    name: str | None
    """The unique package name within its ecosystem."""


class Vulnerability(TypedDict, total=False):
    package: Required[VulnerabilityPackage]
    """The name of the package affected by the vulnerability."""

    patched_versions: str | None
    """The package version(s) that resolve the vulnerability."""

    vulnerable_functions: list[str] | None
    """The functions in the package that are affected."""

    vulnerable_version_range: str | None
    """The range of the package versions affected by the vulnerability."""


class Credit(TypedDict, total=False):
    login: Required[str]
    """The username of the user credited."""

    type: Required[SecurityAdvisoryCreditType]
    """The type of credit the user is receiving."""
