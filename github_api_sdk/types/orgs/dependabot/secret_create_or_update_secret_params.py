

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecretCreateOrUpdateSecretParams"]


class SecretCreateOrUpdateSecretParams(TypedDict, total=False):
    org: Required[str]

    visibility: Required[Literal["all", "private", "selected"]]
    """Which type of organization repositories have access to the organization secret.

    `selected` means only the repositories specified by `selected_repository_ids`
    can access the secret.
    """

    encrypted_value: str
    """
    Value for your secret, encrypted with
    [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
    the public key retrieved from the
    [Get an organization public key](https://docs.github.com/rest/dependabot/secrets#get-an-organization-public-key)
    endpoint.
    """

    key_id: str
    """ID of the key you used to encrypt the secret."""

    selected_repository_ids: list[str]
    """An array of repository ids that can access the organization secret.

    You can only provide a list of repository ids when the `visibility` is set to
    `selected`. You can manage the list of selected repositories using the
    [List selected repositories for an organization secret](https://docs.github.com/rest/dependabot/secrets#list-selected-repositories-for-an-organization-secret),
    [Set selected repositories for an organization secret](https://docs.github.com/rest/dependabot/secrets#set-selected-repositories-for-an-organization-secret),
    and
    [Remove selected repository from an organization secret](https://docs.github.com/rest/dependabot/secrets#remove-selected-repository-from-an-organization-secret)
    endpoints.
    """
