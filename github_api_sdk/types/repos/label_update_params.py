

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LabelUpdateParams"]


class LabelUpdateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    color: str
    """
    The [hexadecimal color code](http://www.color-hex.com/) for the label, without
    the leading `#`.
    """

    description: str
    """A short description of the label. Must be 100 characters or fewer."""

    new_name: str
    """The new name of the label.

    Emoji can be added to label names, using either native emoji or colon-style
    markup. For example, typing `:strawberry:` will render the emoji
    ![:strawberry:](https://github.githubassets.com/images/icons/emoji/unicode/1f353.png ":strawberry:").
    For a full list of available emoji and codes, see
    "[Emoji cheat sheet](https://github.com/ikatyang/emoji-cheat-sheet)."
    """
