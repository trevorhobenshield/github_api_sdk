

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["DeploymentBranchPolicyCreateParams"]


class DeploymentBranchPolicyCreateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    name: Required[str]
    """
    The name pattern that branches or tags must match in order to deploy to the
    environment.

    Wildcard characters will not match `/`. For example, to match branches that
    begin with `release/` and contain an additional single slash, use `release/*/*`.
    For more information about pattern matching syntax, see the
    [Ruby File.fnmatch documentation](https://ruby-doc.org/core-2.5.1/File.html#method-c-fnmatch).
    """

    type: Literal["branch", "tag"]
    """Whether this rule targets a branch or tag"""
