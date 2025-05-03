

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SecretCreateOrUpdateParams"]


class SecretCreateOrUpdateParams(TypedDict, total=False):
    org: Required[str]

    visibility: Required[Literal["all", "private", "selected"]]
    """Which type of organization repositories have access to the organization secret.

    `selected` means only the repositories specified by `selected_repository_ids`
    can access the secret.
    """

    encrypted_value: str
    """
    The value for your secret, encrypted with
    [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
    the public key retrieved from the
    [Get an organization public key](https://docs.github.com/rest/codespaces/organization-secrets#get-an-organization-public-key)
    endpoint.
    """

    key_id: str
    """The ID of the key you used to encrypt the secret."""

    selected_repository_ids: Iterable[int]
    """An array of repository IDs that can access the organization secret.

    You can only provide a list of repository IDs when the `visibility` is set to
    `selected`. You can manage the list of selected repositories using the
    [List selected repositories for an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#list-selected-repositories-for-an-organization-secret),
    [Set selected repositories for an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#set-selected-repositories-for-an-organization-secret),
    and
    [Remove selected repository from an organization secret](https://docs.github.com/rest/codespaces/organization-secrets#remove-selected-repository-from-an-organization-secret)
    endpoints.
    """
