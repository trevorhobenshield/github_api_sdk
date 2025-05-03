

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SecretCreateOrUpdateParams"]


class SecretCreateOrUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    environment_name: Required[str]

    encrypted_value: Required[str]
    """
    Value for your secret, encrypted with
    [LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages) using
    the public key retrieved from the
    [Get an environment public key](https://docs.github.com/rest/actions/secrets#get-an-environment-public-key)
    endpoint.
    """

    key_id: Required[str]
    """ID of the key you used to encrypt the secret."""
