

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["CodespaceCreateParams", "Variant0", "Variant1", "Variant1PullRequest"]


class Variant0(TypedDict, total=False):
    repository_id: Required[int]
    """Repository id for this codespace"""

    client_ip: str
    """IP for location auto-detection when proxying a request"""

    devcontainer_path: str
    """Path to devcontainer.json config to use for this codespace"""

    display_name: str
    """Display name for this codespace"""

    geo: Literal["EuropeWest", "SoutheastAsia", "UsEast", "UsWest"]
    """The geographic area for this codespace.

    If not specified, the value is assigned by IP. This property replaces
    `location`, which is closing down.
    """

    idle_timeout_minutes: int
    """Time in minutes before codespace stops from inactivity"""

    location: str
    """The requested location for a new codespace.

    Best efforts are made to respect this upon creation. Assigned by IP if not
    provided.
    """

    machine: str
    """Machine type to use for this codespace"""

    multi_repo_permissions_opt_out: bool
    """Whether to authorize requested permissions from devcontainer.json"""

    ref: str
    """Git ref (typically a branch name) for this codespace"""

    retention_period_minutes: int
    """Duration in minutes after codespace has gone idle in which it will be deleted.

    Must be integer minutes between 0 and 43200 (30 days).
    """

    working_directory: str
    """Working directory for this codespace"""


class Variant1(TypedDict, total=False):
    pull_request: Required[Variant1PullRequest]
    """Pull request number for this codespace"""

    devcontainer_path: str
    """Path to devcontainer.json config to use for this codespace"""

    geo: Literal["EuropeWest", "SoutheastAsia", "UsEast", "UsWest"]
    """The geographic area for this codespace.

    If not specified, the value is assigned by IP. This property replaces
    `location`, which is closing down.
    """

    idle_timeout_minutes: int
    """Time in minutes before codespace stops from inactivity"""

    location: str
    """The requested location for a new codespace.

    Best efforts are made to respect this upon creation. Assigned by IP if not
    provided.
    """

    machine: str
    """Machine type to use for this codespace"""

    working_directory: str
    """Working directory for this codespace"""


class Variant1PullRequest(TypedDict, total=False):
    pull_request_number: Required[int]
    """Pull request number"""

    repository_id: Required[int]
    """Repository id for this codespace"""


CodespaceCreateParams: TypeAlias = Union[Variant0, Variant1]
