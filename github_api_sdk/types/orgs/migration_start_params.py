

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MigrationStartParams"]


class MigrationStartParams(TypedDict, total=False):
    repositories: Required[list[str]]
    """A list of arrays indicating which repositories should be migrated."""

    exclude: list[Literal["repositories"]]
    """
    Exclude related items from being returned in the response in order to improve
    performance of the request.
    """

    exclude_attachments: bool
    """
    Indicates whether attachments should be excluded from the migration (to reduce
    migration archive file size).
    """

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
    """Indicates whether projects owned by the organization or users should be
    excluded.

    from the migration.
    """

    exclude_releases: bool
    """
    Indicates whether releases should be excluded from the migration (to reduce
    migration archive file size).
    """

    lock_repositories: bool
    """
    Indicates whether repositories should be locked (to prevent manipulation) while
    migrating data.
    """

    org_metadata_only: bool
    """
    Indicates whether this should only include organization metadata (repositories
    array should be empty and will ignore other flags).
    """
