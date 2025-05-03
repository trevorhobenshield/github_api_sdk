

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleCodeScanningParam", "Parameters", "ParametersCodeScanningTool"]


class ParametersCodeScanningTool(TypedDict, total=False):
    alerts_threshold: Required[Literal["none", "errors", "errors_and_warnings", "all"]]
    """
    The severity level at which code scanning results that raise alerts block a
    reference update. For more information on alert severity levels, see
    "[About code scanning alerts](https://docs.github.com/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels)."
    """

    security_alerts_threshold: Required[Literal["none", "critical", "high_or_higher", "medium_or_higher", "all"]]
    """
    The severity level at which code scanning results that raise security alerts
    block a reference update. For more information on security severity levels, see
    "[About code scanning alerts](https://docs.github.com/code-security/code-scanning/managing-code-scanning-alerts/about-code-scanning-alerts#about-alert-severity-and-security-severity-levels)."
    """

    tool: Required[str]
    """The name of a code scanning tool"""


class Parameters(TypedDict, total=False):
    code_scanning_tools: Required[Iterable[ParametersCodeScanningTool]]
    """Tools that must provide code scanning results for this rule to pass."""


class RepositoryRuleCodeScanningParam(TypedDict, total=False):
    type: Required[Literal["code_scanning"]]

    parameters: Parameters
