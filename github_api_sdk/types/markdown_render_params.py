

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MarkdownRenderParams"]


class MarkdownRenderParams(TypedDict, total=False):
    text: Required[str]
    """The Markdown text to render in HTML."""

    context: str
    """The repository context to use when creating references in `gfm` mode.

    For example, setting `context` to `octo-org/octo-repo` will change the text
    `#42` into an HTML link to issue 42 in the `octo-org/octo-repo` repository.
    """

    mode: Literal["markdown", "gfm"]
    """The rendering mode."""
