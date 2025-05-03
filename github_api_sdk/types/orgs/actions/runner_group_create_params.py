

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RunnerGroupCreateParams"]


class RunnerGroupCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the runner group."""

    allows_public_repositories: bool
    """Whether the runner group can be used by `public` repositories."""

    network_configuration_id: str
    """The identifier of a hosted compute network configuration."""

    restricted_to_workflows: bool
    """
    If `true`, the runner group will be restricted to running only the workflows
    specified in the `selected_workflows` array.
    """

    runners: Iterable[int]
    """List of runner IDs to add to the runner group."""

    selected_repository_ids: Iterable[int]
    """List of repository IDs that can access the runner group."""

    selected_workflows: list[str]
    """List of workflows the runner group should be allowed to run.

    This setting will be ignored unless `restricted_to_workflows` is set to `true`.
    """

    visibility: Literal["selected", "all", "private"]
    """Visibility of a runner group.

    You can select all repositories, select individual repositories, or limit access
    to private repositories.
    """
