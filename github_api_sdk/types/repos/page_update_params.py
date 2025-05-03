

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["PageUpdateParams", "Source", "SourceUnionMember1"]


class PageUpdateParams(TypedDict, total=False):
    owner: Required[str]

    build_type: Literal["legacy", "workflow"]
    """The process by which the GitHub Pages site will be built.

    `workflow` means that the site is built by a custom GitHub Actions workflow.
    `legacy` means that the site is built by GitHub when changes are pushed to a
    specific branch.
    """

    cname: str | None
    """Specify a custom domain for the repository.

    Sending a `null` value will remove the custom domain. For more about custom
    domains, see
    "[Using a custom domain with GitHub Pages](https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site)."
    """

    https_enforced: bool
    """Specify whether HTTPS should be enforced for the repository."""

    source: Source
    """Update the source for the repository.

    Must include the branch name, and may optionally specify the subdirectory
    `/docs`. Possible values are `"gh-pages"`, `"master"`, and `"master /docs"`.
    """


class SourceUnionMember1(TypedDict, total=False):
    branch: Required[str]
    """The repository branch used to publish your site's source files."""

    path: Required[Literal["/", "/docs"]]
    """The repository directory that includes the source files for the Pages site.

    Allowed paths are `/` or `/docs`.
    """


Source: TypeAlias = Union[Literal["gh-pages", "master", "master /docs"], SourceUnionMember1]
