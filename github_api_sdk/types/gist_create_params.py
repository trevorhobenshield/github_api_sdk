

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["GistCreateParams", "Files"]


class GistCreateParams(TypedDict, total=False):
    files: Required[dict[str, Files]]
    """Names and content for the files that make up the gist"""

    description: str
    """Description of the gist"""

    public: bool | Literal["true", "false"]
    """Flag indicating whether the gist is public"""


class Files(TypedDict, total=False):
    content: Required[str]
    """Content of the file"""
