

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PageCreateParams", "Source"]


class PageCreateParams(TypedDict, total=False):
    owner: Required[str]

    build_type: Literal["legacy", "workflow"]
    """The process in which the Page will be built.

    Possible values are `"legacy"` and `"workflow"`.
    """

    source: Source
    """The source branch and directory used to publish your Pages site."""


class Source(TypedDict, total=False):
    branch: Required[str]
    """The repository branch used to publish your site's source files."""

    path: Literal["/", "/docs"]
    """The repository directory that includes the source files for the Pages site.

    Allowed paths are `/` or `/docs`. Default: `/`
    """
