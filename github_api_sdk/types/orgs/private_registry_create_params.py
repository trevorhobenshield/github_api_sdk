

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PrivateRegistryCreateParams"]


class PrivateRegistryCreateParams(TypedDict, total=False):
    encrypted_value: Required[str]
    """
    The value for your secret, encrypted with
    [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
    the public key retrieved from the
    [Get private registries public key for an organization](https://docs.github.com/rest/private-registries/organization-configurations#get-private-registries-public-key-for-an-organization)
    endpoint.
    """

    key_id: Required[str]
    """The ID of the key you used to encrypt the secret."""

    registry_type: Required[Literal["maven_repository"]]
    """The registry type."""

    visibility: Required[Literal["all", "private", "selected"]]
    """Which type of organization repositories have access to the private registry.

    `selected` means only the repositories specified by `selected_repository_ids`
    can access the private registry.
    """

    selected_repository_ids: Iterable[int]
    """An array of repository IDs that can access the organization private registry.

    You can only provide a list of repository IDs when `visibility` is set to
    `selected`. You can manage the list of selected repositories using the
    [Update a private registry for an organization](https://docs.github.com/rest/private-registries/organization-configurations#update-a-private-registry-for-an-organization)
    endpoint. This field should be omitted if `visibility` is set to `all` or
    `private`.
    """

    username: str | None
    """The username to use when authenticating with the private registry.

    This field should be omitted if the private registry does not require a username
    for authentication.
    """
