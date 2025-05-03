

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["RepositorySetParams"]


class RepositorySetParams(TypedDict, total=False):
    selected_repository_ids: Required[Iterable[int]]
    """An array of repository ids for which a codespace can access the secret.

    You can manage the list of selected repositories using the
    [List selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#list-selected-repositories-for-a-user-secret),
    [Add a selected repository to a user secret](https://docs.github.com/rest/codespaces/secrets#add-a-selected-repository-to-a-user-secret),
    and
    [Remove a selected repository from a user secret](https://docs.github.com/rest/codespaces/secrets#remove-a-selected-repository-from-a-user-secret)
    endpoints.
    """
