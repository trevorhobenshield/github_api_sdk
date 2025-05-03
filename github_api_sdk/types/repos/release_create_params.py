

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReleaseCreateParams"]


class ReleaseCreateParams(TypedDict, total=False):
    owner: Required[str]

    tag_name: Required[str]
    """The name of the tag."""

    body: str
    """Text describing the contents of the tag."""

    discussion_category_name: str
    """
    If specified, a discussion of the specified category is created and linked to
    the release. The value must be a category that already exists in the repository.
    For more information, see
    "[Managing categories for discussions in your repository](https://docs.github.com/discussions/managing-discussions-for-your-community/managing-categories-for-discussions-in-your-repository)."
    """

    draft: bool
    """
    `true` to create a draft (unpublished) release, `false` to create a published
    one.
    """

    generate_release_notes: bool
    """Whether to automatically generate the name and body for this release.

    If `name` is specified, the specified name will be used; otherwise, a name will
    be automatically generated. If `body` is specified, the body will be pre-pended
    to the automatically generated notes.
    """

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
    """`true` to identify the release as a prerelease.

    `false` to identify the release as a full release.
    """

    target_commitish: str
    """Specifies the commitish value that determines where the Git tag is created from.

    Can be any branch or commit SHA. Unused if the Git tag already exists. Default:
    the repository's default branch.
    """
