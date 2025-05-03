

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MarkdownRenderRawParams"]


class MarkdownRenderRawParams(TypedDict, total=False):
    body: str
