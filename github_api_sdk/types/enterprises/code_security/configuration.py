

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = [
    "Configuration",
    "CodeScanningDefaultSetupOptions",
    "DependencyGraphAutosubmitActionOptions",
    "SecretScanningDelegatedBypassOptions",
    "SecretScanningDelegatedBypassOptionsReviewer",
]


class CodeScanningDefaultSetupOptions(BaseModel):
    runner_label: Optional[str] = None
    """The label of the runner to use for code scanning when runner_type is 'labeled'."""

    runner_type: Optional[Literal["standard", "labeled", "not_set"]] = None
    """Whether to use labeled runners or standard GitHub runners."""


class DependencyGraphAutosubmitActionOptions(BaseModel):
    labeled_runners: Optional[bool] = None
    """
    Whether to use runners labeled with 'dependency-submission' or standard GitHub
    runners.
    """


class SecretScanningDelegatedBypassOptionsReviewer(BaseModel):
    reviewer_id: int
    """The ID of the team or role selected as a bypass reviewer"""

    reviewer_type: Literal["TEAM", "ROLE"]
    """The type of the bypass reviewer"""


class SecretScanningDelegatedBypassOptions(BaseModel):
    reviewers: Optional[List[SecretScanningDelegatedBypassOptionsReviewer]] = None
    """The bypass reviewers for secret scanning delegated bypass"""


class Configuration(BaseModel):
    id: Optional[int] = None
    """The ID of the code security configuration"""

    advanced_security: Optional[Literal["enabled", "disabled"]] = None
    """The enablement status of GitHub Advanced Security"""

    code_scanning_default_setup: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of code scanning default setup"""

    code_scanning_default_setup_options: Optional[CodeScanningDefaultSetupOptions] = None
    """Feature options for code scanning default setup"""

    code_scanning_delegated_alert_dismissal: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of code scanning delegated alert dismissal"""

    created_at: Optional[datetime] = None

    dependabot_alerts: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of Dependabot alerts"""

    dependabot_security_updates: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of Dependabot security updates"""

    dependency_graph: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of Dependency Graph"""

    dependency_graph_autosubmit_action: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of Automatic dependency submission"""

    dependency_graph_autosubmit_action_options: Optional[DependencyGraphAutosubmitActionOptions] = None
    """Feature options for Automatic dependency submission"""

    description: Optional[str] = None
    """A description of the code security configuration"""

    enforcement: Optional[Literal["enforced", "unenforced"]] = None
    """The enforcement status for a security configuration"""

    html_url: Optional[str] = None
    """The URL of the configuration"""

    name: Optional[str] = None
    """The name of the code security configuration.

    Must be unique within the organization.
    """

    private_vulnerability_reporting: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of private vulnerability reporting"""

    secret_scanning: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of secret scanning"""

    secret_scanning_delegated_alert_dismissal: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of secret scanning delegated alert dismissal"""

    secret_scanning_delegated_bypass: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of secret scanning delegated bypass"""

    secret_scanning_delegated_bypass_options: Optional[SecretScanningDelegatedBypassOptions] = None
    """Feature options for secret scanning delegated bypass"""

    secret_scanning_generic_secrets: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of Copilot secret scanning"""

    secret_scanning_non_provider_patterns: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of secret scanning non-provider patterns"""

    secret_scanning_push_protection: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of secret scanning push protection"""

    secret_scanning_validity_checks: Optional[Literal["enabled", "disabled", "not_set"]] = None
    """The enablement status of secret scanning validity checks"""

    target_type: Optional[Literal["global", "organization", "enterprise"]] = None
    """The type of the code security configuration."""

    updated_at: Optional[datetime] = None

    url: Optional[str] = None
    """The URL of the configuration"""
