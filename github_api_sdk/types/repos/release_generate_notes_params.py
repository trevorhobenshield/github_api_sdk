

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ReleaseGenerateNotesParams"]


class ReleaseGenerateNotesParams(TypedDict, total=False):
    owner: Required[str]

    tag_name: Required[str]
    """The tag name for the release. This can be an existing tag or a new one."""

    configuration_file_path: str
    """
    Specifies a path to a file in the repository containing configuration settings
    used for generating the release notes. If unspecified, the configuration file
    located in the repository at '.github/release.yml' or '.github/release.yaml'
    will be used. If that is not present, the default configuration will be used.
    """

    previous_tag_name: str
    """The name of the previous tag to use as the starting point for the release notes.

    Use to manually specify the range for the set of changes considered as part this
    release.
    """

    target_commitish: str
    """Specifies the commitish value that will be the target for the release's tag.

    Required if the supplied tag_name does not reference an existing tag. Ignored if
    the tag_name already exists.
    """
