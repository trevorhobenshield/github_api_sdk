

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleRequiredDeploymentsParam", "Parameters"]


class Parameters(TypedDict, total=False):
    required_deployment_environments: Required[list[str]]
    """
    The environments that must be successfully deployed to before branches can be
    merged.
    """


class RepositoryRuleRequiredDeploymentsParam(TypedDict, total=False):
    type: Required[Literal["required_deployments"]]

    parameters: Parameters
