

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypedDict

__all__ = ["SecretCreateOrUpdateParams"]


class SecretCreateOrUpdateParams(TypedDict, total=False):
    key_id: Required[str]
    """ID of the key you used to encrypt the secret."""

    encrypted_value: str
    """
    Value for your secret, encrypted with
    [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
    the public key retrieved from the
    [Get the public key for the authenticated user](https://docs.github.com/rest/codespaces/secrets#get-public-key-for-the-authenticated-user)
    endpoint.
    """

    selected_repository_ids: list[int | str]
    """An array of repository ids that can access the user secret.

    You can manage the list of selected repositories using the
    [List selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#list-selected-repositories-for-a-user-secret),
    [Set selected repositories for a user secret](https://docs.github.com/rest/codespaces/secrets#set-selected-repositories-for-a-user-secret),
    and
    [Remove a selected repository from a user secret](https://docs.github.com/rest/codespaces/secrets#remove-a-selected-repository-from-a-user-secret)
    endpoints.
    """
