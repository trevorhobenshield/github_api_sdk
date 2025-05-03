

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleRequiredStatusChecks", "Parameters", "ParametersRequiredStatusCheck"]


class ParametersRequiredStatusCheck(BaseModel):
    context: str
    """The status check context name that must be present on the commit."""

    integration_id: Optional[int] = None
    """The optional integration ID that this status check must originate from."""


class Parameters(BaseModel):
    required_status_checks: List[ParametersRequiredStatusCheck]
    """Status checks that are required."""

    strict_required_status_checks_policy: bool
    """
    Whether pull requests targeting a matching branch must be tested with the latest
    code. This setting will not take effect unless at least one status check is
    enabled.
    """

    do_not_enforce_on_create: Optional[bool] = None
    """
    Allow repositories and branches to be created if a check would otherwise
    prohibit it.
    """


class RepositoryRuleRequiredStatusChecks(BaseModel):
    type: Literal["required_status_checks"]

    parameters: Optional[Parameters] = None
