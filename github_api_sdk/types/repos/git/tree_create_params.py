

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TreeCreateParams", "Tree"]


class TreeCreateParams(TypedDict, total=False):
    owner: Required[str]

    tree: Required[Iterable[Tree]]
    """Objects (of `path`, `mode`, `type`, and `sha`) specifying a tree structure."""

    base_tree: str
    """
    The SHA1 of an existing Git tree object which will be used as the base for the
    new tree. If provided, a new Git tree object will be created from entries in the
    Git tree object pointed to by `base_tree` and entries defined in the `tree`
    parameter. Entries defined in the `tree` parameter will overwrite items from
    `base_tree` with the same `path`. If you're creating new changes on a branch,
    then normally you'd set `base_tree` to the SHA1 of the Git tree object of the
    current latest commit on the branch you're working on. If not provided, GitHub
    will create a new Git tree object from only the entries defined in the `tree`
    parameter. If you create a new commit pointing to such a tree, then all files
    which were a part of the parent commit's tree and were not defined in the `tree`
    parameter will be listed as deleted by the new commit.
    """


class Tree(TypedDict, total=False):
    content: str
    """The content you want this file to have.

    GitHub will write this blob out and use that SHA for this entry. Use either
    this, or `tree.sha`.

    **Note:** Use either `tree.sha` or `content` to specify the contents of the
    entry. Using both `tree.sha` and `content` will return an error.
    """

    mode: Literal["100644", "100755", "040000", "160000", "120000"]
    """
    The file mode; one of `100644` for file (blob), `100755` for executable (blob),
    `040000` for subdirectory (tree), `160000` for submodule (commit), or `120000`
    for a blob that specifies the path of a symlink.
    """

    path: str
    """The file referenced in the tree."""

    sha: str | None
    """The SHA1 checksum ID of the object in the tree.

    Also called `tree.sha`. If the value is `null` then the file will be deleted.

    **Note:** Use either `tree.sha` or `content` to specify the contents of the
    entry. Using both `tree.sha` and `content` will return an error.
    """

    type: Literal["blob", "tree", "commit"]
    """Either `blob`, `tree`, or `commit`."""
