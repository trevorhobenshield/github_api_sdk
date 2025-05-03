

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "SecurityAndAnalysis",
    "AdvancedSecurity",
    "CodeSecurity",
    "DependabotSecurityUpdates",
    "SecretScanning",
    "SecretScanningAIDetection",
    "SecretScanningNonProviderPatterns",
    "SecretScanningPushProtection",
]


class AdvancedSecurity(BaseModel):
    status: Optional[Literal["enabled", "disabled"]] = None


class CodeSecurity(BaseModel):
    status: Optional[Literal["enabled", "disabled"]] = None


class DependabotSecurityUpdates(BaseModel):
    status: Optional[Literal["enabled", "disabled"]] = None
    """The enablement status of Dependabot security updates for the repository."""


class SecretScanning(BaseModel):
    status: Optional[Literal["enabled", "disabled"]] = None


class SecretScanningAIDetection(BaseModel):
    status: Optional[Literal["enabled", "disabled"]] = None


class SecretScanningNonProviderPatterns(BaseModel):
    status: Optional[Literal["enabled", "disabled"]] = None


class SecretScanningPushProtection(BaseModel):
    status: Optional[Literal["enabled", "disabled"]] = None


class SecurityAndAnalysis(BaseModel):
    advanced_security: Optional[AdvancedSecurity] = None

    code_security: Optional[CodeSecurity] = None

    dependabot_security_updates: Optional[DependabotSecurityUpdates] = None
    """Enable or disable Dependabot security updates for the repository."""

    secret_scanning: Optional[SecretScanning] = None

    secret_scanning_ai_detection: Optional[SecretScanningAIDetection] = None

    secret_scanning_non_provider_patterns: Optional[SecretScanningNonProviderPatterns] = None

    secret_scanning_push_protection: Optional[SecretScanningPushProtection] = None
