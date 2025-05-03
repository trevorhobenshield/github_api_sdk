

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RepoCreateFromTemplateParams"]


class RepoCreateFromTemplateParams(TypedDict, total=False):
    template_owner: Required[str]

    name: Required[str]
    """The name of the new repository."""

    description: str
    """A short description of the new repository."""

    include_all_branches: bool
    """
    Set to `true` to include the directory structure and files from all branches in
    the template repository, and not just the default branch. Default: `false`.
    """

    owner: str
    """The organization or person who will own the new repository.

    To create a new repository in an organization, the authenticated user must be a
    member of the specified organization.
    """

    private: bool
    """
    Either `true` to create a new private repository or `false` to create a new
    public one.
    """
