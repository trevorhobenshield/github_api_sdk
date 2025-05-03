

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..orgs.simple_user import SimpleUser
from ..orgs.full_repository import FullRepository
from ..orgs.members.nullable_codespace_machine import NullableCodespaceMachine

__all__ = ["CodespacePublishResponse", "GitStatus", "RuntimeConstraints"]


class GitStatus(BaseModel):
    ahead: Optional[int] = None
    """The number of commits the local repository is ahead of the remote."""

    behind: Optional[int] = None
    """The number of commits the local repository is behind the remote."""

    has_uncommitted_changes: Optional[bool] = None
    """Whether the local repository has uncommitted changes."""

    has_unpushed_changes: Optional[bool] = None
    """Whether the local repository has unpushed changes."""

    ref: Optional[str] = None
    """The current branch (or SHA if in detached HEAD state) of the local repository."""


class RuntimeConstraints(BaseModel):
    allowed_port_privacy_settings: Optional[List[str]] = None
    """The privacy settings a user can select from when forwarding a port."""


class CodespacePublishResponse(BaseModel):
    id: int

    billable_owner: SimpleUser
    """A GitHub user."""

    created_at: datetime

    environment_id: Optional[str] = None
    """UUID identifying this codespace's environment."""

    git_status: GitStatus
    """Details about the codespace's git repository."""

    idle_timeout_minutes: Optional[int] = None
    """
    The number of minutes of inactivity after which this codespace will be
    automatically stopped.
    """

    last_used_at: datetime
    """Last known time this codespace was started."""

    location: Literal["EastUs", "SouthEastAsia", "WestEurope", "WestUs2"]
    """The initally assigned location of a new codespace."""

    machine: Optional[NullableCodespaceMachine] = None
    """A description of the machine powering a codespace."""

    machines_url: str
    """API URL to access available alternate machine types for this codespace."""

    name: str
    """Automatically generated name of this codespace."""

    owner: SimpleUser
    """A GitHub user."""

    prebuild: Optional[bool] = None
    """Whether the codespace was created from a prebuild."""

    pulls_url: Optional[str] = None
    """API URL for the Pull Request associated with this codespace, if any."""

    recent_folders: List[str]

    repository: FullRepository
    """Full Repository"""

    start_url: str
    """API URL to start this codespace."""

    state: Literal[
        "Unknown",
        "Created",
        "Queued",
        "Provisioning",
        "Available",
        "Awaiting",
        "Unavailable",
        "Deleted",
        "Moved",
        "Shutdown",
        "Archived",
        "Starting",
        "ShuttingDown",
        "Failed",
        "Exporting",
        "Updating",
        "Rebuilding",
    ]
    """State of this codespace."""

    stop_url: str
    """API URL to stop this codespace."""

    updated_at: datetime

    url: str
    """API URL for this codespace."""

    web_url: str
    """URL to access this codespace on the web."""

    devcontainer_path: Optional[str] = None
    """Path to devcontainer.json from repo root used to create Codespace."""

    display_name: Optional[str] = None
    """Display name for this codespace."""

    idle_timeout_notice: Optional[str] = None
    """
    Text to show user when codespace idle timeout minutes has been overriden by an
    organization policy
    """

    pending_operation: Optional[bool] = None
    """Whether or not a codespace has a pending async operation.

    This would mean that the codespace is temporarily unavailable. The only thing
    that you can do with a codespace in this state is delete it.
    """

    pending_operation_disabled_reason: Optional[str] = None
    """Text to show user when codespace is disabled by a pending operation"""

    publish_url: Optional[str] = None
    """API URL to publish this codespace to a new repository."""

    retention_expires_at: Optional[datetime] = None
    """
    When a codespace will be auto-deleted based on the "retention_period_minutes"
    and "last_used_at"
    """

    retention_period_minutes: Optional[int] = None
    """Duration in minutes after codespace has gone idle in which it will be deleted.

    Must be integer minutes between 0 and 43200 (30 days).
    """

    runtime_constraints: Optional[RuntimeConstraints] = None
