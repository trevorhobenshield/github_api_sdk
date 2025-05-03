

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleRequiredStatusChecksParam", "Parameters", "ParametersRequiredStatusCheck"]


class ParametersRequiredStatusCheck(TypedDict, total=False):
    context: Required[str]
    """The status check context name that must be present on the commit."""

    integration_id: int
    """The optional integration ID that this status check must originate from."""


class Parameters(TypedDict, total=False):
    required_status_checks: Required[Iterable[ParametersRequiredStatusCheck]]
    """Status checks that are required."""

    strict_required_status_checks_policy: Required[bool]
    """
    Whether pull requests targeting a matching branch must be tested with the latest
    code. This setting will not take effect unless at least one status check is
    enabled.
    """

    do_not_enforce_on_create: bool
    """
    Allow repositories and branches to be created if a check would otherwise
    prohibit it.
    """


class RepositoryRuleRequiredStatusChecksParam(TypedDict, total=False):
    type: Required[Literal["required_status_checks"]]

    parameters: Parameters
