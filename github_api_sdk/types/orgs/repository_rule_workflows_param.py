

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RepositoryRuleWorkflowsParam", "Parameters", "ParametersWorkflow"]


class ParametersWorkflow(TypedDict, total=False):
    path: Required[str]
    """The path to the workflow file"""

    repository_id: Required[int]
    """The ID of the repository where the workflow is defined"""

    ref: str
    """The ref (branch or tag) of the workflow file to use"""

    sha: str
    """The commit SHA of the workflow file to use"""


class Parameters(TypedDict, total=False):
    workflows: Required[Iterable[ParametersWorkflow]]
    """Workflows that must pass for this rule to pass."""

    do_not_enforce_on_create: bool
    """
    Allow repositories and branches to be created if a check would otherwise
    prohibit it.
    """


class RepositoryRuleWorkflowsParam(TypedDict, total=False):
    type: Required[Literal["workflows"]]

    parameters: Parameters
