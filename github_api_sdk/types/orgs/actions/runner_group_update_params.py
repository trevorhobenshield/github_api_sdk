

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RunnerGroupUpdateParams"]


class RunnerGroupUpdateParams(TypedDict, total=False):
    org: Required[str]

    name: Required[str]
    """Name of the runner group."""

    allows_public_repositories: bool
    """Whether the runner group can be used by `public` repositories."""

    network_configuration_id: str | None
    """The identifier of a hosted compute network configuration."""

    restricted_to_workflows: bool
    """
    If `true`, the runner group will be restricted to running only the workflows
    specified in the `selected_workflows` array.
    """

    selected_workflows: list[str]
    """List of workflows the runner group should be allowed to run.

    This setting will be ignored unless `restricted_to_workflows` is set to `true`.
    """

    visibility: Literal["selected", "all", "private"]
    """Visibility of a runner group.

    You can select all repositories, select individual repositories, or all private
    repositories.
    """
