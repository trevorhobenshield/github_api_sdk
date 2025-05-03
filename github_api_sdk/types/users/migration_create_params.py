

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MigrationCreateParams"]


class MigrationCreateParams(TypedDict, total=False):
    repositories: Required[list[str]]

    exclude: list[Literal["repositories"]]
    """Exclude attributes from the API response to improve performance"""

    exclude_attachments: bool
    """Do not include attachments in the migration"""

    exclude_git_data: bool
    """
    Indicates whether the repository git data should be excluded from the migration.
    """

    exclude_metadata: bool
    """
    Indicates whether metadata should be excluded and only git source should be
    included for the migration.
    """

    exclude_owner_projects: bool
    """
    Indicates whether projects owned by the organization or users should be
    excluded.
    """

    exclude_releases: bool
    """Do not include releases in the migration"""

    lock_repositories: bool
    """Lock the repositories being migrated at the start of the migration"""

    org_metadata_only: bool
    """
    Indicates whether this should only include organization metadata (repositories
    array should be empty and will ignore other flags).
    """
