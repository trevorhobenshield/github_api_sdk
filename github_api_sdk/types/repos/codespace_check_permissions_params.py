

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CodespaceCheckPermissionsParams"]


class CodespaceCheckPermissionsParams(TypedDict, total=False):
    owner: Required[str]

    devcontainer_path: Required[str]
    """Path to the devcontainer.json configuration to use for the permission check."""

    ref: Required[str]
    """
    The git reference that points to the location of the devcontainer configuration
    to use for the permission check. The value of `ref` will typically be a branch
    name (`heads/BRANCH_NAME`). For more information, see
    "[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)"
    in the Git documentation.
    """
