

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SSHSigningKeyCreateParams"]


class SSHSigningKeyCreateParams(TypedDict, total=False):
    key: Required[str]
    """The public SSH key to add to your GitHub account.

    For more information, see
    "[Checking for existing SSH keys](https://docs.github.com/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)."
    """

    title: str
    """A descriptive name for the new key."""
