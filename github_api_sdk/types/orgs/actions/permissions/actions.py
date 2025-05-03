

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["Actions"]


class Actions(BaseModel):
    github_owned_allowed: Optional[bool] = None
    """Whether GitHub-owned actions are allowed.

    For example, this includes the actions in the `actions` organization.
    """

    patterns_allowed: Optional[List[str]] = None
    """
    Specifies a list of string-matching patterns to allow specific action(s) and
    reusable workflow(s). Wildcards, tags, and SHAs are allowed. For example,
    `monalisa/octocat@*`, `monalisa/octocat@v2`, `monalisa/*`.

    > [!NOTE] The `patterns_allowed` setting only applies to public repositories.
    """

    verified_allowed: Optional[bool] = None
    """Whether actions from GitHub Marketplace verified creators are allowed.

    Set to `true` to allow all actions by GitHub Marketplace verified creators.
    """
