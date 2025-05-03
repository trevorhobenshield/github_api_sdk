

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReleaseUpdateParams"]


class ReleaseUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    body: str
    """Text describing the contents of the tag."""

    discussion_category_name: str
    """
    If specified, a discussion of the specified category is created and linked to
    the release. The value must be a category that already exists in the repository.
    If there is already a discussion linked to the release, this parameter is
    ignored. For more information, see
    "[Managing categories for discussions in your repository](https://docs.github.com/discussions/managing-discussions-for-your-community/managing-categories-for-discussions-in-your-repository)."
    """

    draft: bool
    """`true` makes the release a draft, and `false` publishes the release."""

    make_latest: Literal["true", "false", "legacy"]
    """
    Specifies whether this release should be set as the latest release for the
    repository. Drafts and prereleases cannot be set as latest. Defaults to `true`
    for newly published releases. `legacy` specifies that the latest release should
    be determined based on the release creation date and higher semantic version.
    """

    name: str
    """The name of the release."""

    prerelease: bool
    """
    `true` to identify the release as a prerelease, `false` to identify the release
    as a full release.
    """

    tag_name: str
    """The name of the tag."""

    target_commitish: str
    """Specifies the commitish value that determines where the Git tag is created from.

    Can be any branch or commit SHA. Unused if the Git tag already exists. Default:
    the repository's default branch.
    """
