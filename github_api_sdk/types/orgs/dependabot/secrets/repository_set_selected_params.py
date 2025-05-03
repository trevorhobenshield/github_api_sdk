

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RepositorySetSelectedParams"]


class RepositorySetSelectedParams(TypedDict, total=False):
    org: Required[str]

    selected_repository_ids: Required[Iterable[int]]
    """An array of repository ids that can access the organization secret.

    You can only provide a list of repository ids when the `visibility` is set to
    `selected`. You can add and remove individual repositories using the
    [Set selected repositories for an organization secret](https://docs.github.com/rest/dependabot/secrets#set-selected-repositories-for-an-organization-secret)
    and
    [Remove selected repository from an organization secret](https://docs.github.com/rest/dependabot/secrets#remove-selected-repository-from-an-organization-secret)
    endpoints.
    """
