

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ...enterprises.code_security.scanning_options_param import ScanningOptionsParam

__all__ = [
    "ConfigurationUpdateParams",
    "DependencyGraphAutosubmitActionOptions",
    "SecretScanningDelegatedBypassOptions",
    "SecretScanningDelegatedBypassOptionsReviewer",
]


class ConfigurationUpdateParams(TypedDict, total=False):
    org: Required[str]

    advanced_security: Literal["enabled", "disabled"]
    """The enablement status of GitHub Advanced Security"""

    code_scanning_default_setup: Literal["enabled", "disabled", "not_set"]
    """The enablement status of code scanning default setup"""

    code_scanning_default_setup_options: ScanningOptionsParam | None
    """Feature options for code scanning default setup"""

    code_scanning_delegated_alert_dismissal: Literal["enabled", "disabled", "not_set"]
    """The enablement status of code scanning delegated alert dismissal"""

    dependabot_alerts: Literal["enabled", "disabled", "not_set"]
    """The enablement status of Dependabot alerts"""

    dependabot_security_updates: Literal["enabled", "disabled", "not_set"]
    """The enablement status of Dependabot security updates"""

    dependency_graph: Literal["enabled", "disabled", "not_set"]
    """The enablement status of Dependency Graph"""

    dependency_graph_autosubmit_action: Literal["enabled", "disabled", "not_set"]
    """The enablement status of Automatic dependency submission"""

    dependency_graph_autosubmit_action_options: DependencyGraphAutosubmitActionOptions
    """Feature options for Automatic dependency submission"""

    description: str
    """A description of the code security configuration"""

    enforcement: Literal["enforced", "unenforced"]
    """The enforcement status for a security configuration"""

    name: str
    """The name of the code security configuration.

    Must be unique within the organization.
    """

    private_vulnerability_reporting: Literal["enabled", "disabled", "not_set"]
    """The enablement status of private vulnerability reporting"""

    secret_scanning: Literal["enabled", "disabled", "not_set"]
    """The enablement status of secret scanning"""

    secret_scanning_delegated_alert_dismissal: Literal["enabled", "disabled", "not_set"]
    """The enablement status of secret scanning delegated alert dismissal"""

    secret_scanning_delegated_bypass: Literal["enabled", "disabled", "not_set"]
    """The enablement status of secret scanning delegated bypass"""

    secret_scanning_delegated_bypass_options: SecretScanningDelegatedBypassOptions
    """Feature options for secret scanning delegated bypass"""

    secret_scanning_generic_secrets: Literal["enabled", "disabled", "not_set"]
    """The enablement status of Copilot secret scanning"""

    secret_scanning_non_provider_patterns: Literal["enabled", "disabled", "not_set"]
    """The enablement status of secret scanning non-provider patterns"""

    secret_scanning_push_protection: Literal["enabled", "disabled", "not_set"]
    """The enablement status of secret scanning push protection"""

    secret_scanning_validity_checks: Literal["enabled", "disabled", "not_set"]
    """The enablement status of secret scanning validity checks"""


class DependencyGraphAutosubmitActionOptions(TypedDict, total=False):
    labeled_runners: bool
    """
    Whether to use runners labeled with 'dependency-submission' or standard GitHub
    runners.
    """


class SecretScanningDelegatedBypassOptionsReviewer(TypedDict, total=False):
    reviewer_id: Required[int]
    """The ID of the team or role selected as a bypass reviewer"""

    reviewer_type: Required[Literal["TEAM", "ROLE"]]
    """The type of the bypass reviewer"""


class SecretScanningDelegatedBypassOptions(TypedDict, total=False):
    reviewers: Iterable[SecretScanningDelegatedBypassOptionsReviewer]
    """The bypass reviewers for secret scanning delegated bypass"""
