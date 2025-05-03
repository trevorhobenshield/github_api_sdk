

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleCodeScanning", "Parameters", "ParametersCodeScanningTool"]


class ParametersCodeScanningTool(BaseModel):
    alerts_threshold: Literal["none", "errors", "errors_and_warnings", "all"]
    """
    The severity level at which code scanning results that raise alerts block a
    reference update. For more information on alert severity levels, see
    "[About code scanning alerts](https://docs.github.com/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels)."
    """

    security_alerts_threshold: Literal["none", "critical", "high_or_higher", "medium_or_higher", "all"]
    """
    The severity level at which code scanning results that raise security alerts
    block a reference update. For more information on security severity levels, see
    "[About code scanning alerts](https://docs.github.com/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels)."
    """

    tool: str
    """The name of a code scanning tool"""


class Parameters(BaseModel):
    code_scanning_tools: List[ParametersCodeScanningTool]
    """Tools that must provide code scanning results for this rule to pass."""


class RepositoryRuleCodeScanning(BaseModel):
    type: Literal["code_scanning"]

    parameters: Optional[Parameters] = None
