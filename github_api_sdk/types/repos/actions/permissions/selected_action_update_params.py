

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SelectedActionUpdateParams"]


class SelectedActionUpdateParams(TypedDict, total=False):
    owner: Required[str]

    github_owned_allowed: bool
    """Whether GitHub-owned actions are allowed.

    For example, this includes the actions in the `actions` organization.
    """

    patterns_allowed: list[str]
    """
    Specifies a list of string-matching patterns to allow specific action(s) and
    reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example,
    `monalisa/octocat@*`, `monalisa/octocat@v2`, `monalisa/*`.

    > [!NOTE] The `patterns_allowed` setting only applies to public repositories.
    """

    verified_allowed: bool
    """Whether actions from GitHub Marketplace verified creators are allowed.

    Set to `true` to allow all actions by GitHub Marketplace verified creators.
    """
