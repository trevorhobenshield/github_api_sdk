

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["Groups"]


class Groups(BaseModel):
    id: float

    allows_public_repositories: bool

    default: bool

    inherited: bool

    name: str

    runners_url: str

    visibility: str

    hosted_runners_url: Optional[str] = None

    inherited_allows_public_repositories: Optional[bool] = None

    network_configuration_id: Optional[str] = None
    """The identifier of a hosted compute network configuration."""

    restricted_to_workflows: Optional[bool] = None
    """
    If `true`, the runner group will be restricted to running only the workflows
    specified in the `selected_workflows` array.
    """

    selected_repositories_url: Optional[str] = None
    """Link to the selected repositories resource for this runner group.

    Not present unless visibility was set to `selected`
    """

    selected_workflows: Optional[List[str]] = None
    """List of workflows the runner group should be allowed to run.

    This setting will be ignored unless `restricted_to_workflows` is set to `true`.
    """

    workflow_restrictions_read_only: Optional[bool] = None
    """
    If `true`, the `restricted_to_workflows` and `selected_workflows` fields cannot
    be modified.
    """
