

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .code_scanning_variant_analysis_language import CodeScanningVariantAnalysisLanguage

__all__ = ["VariantAnalysisCreateParams"]


class VariantAnalysisCreateParams(TypedDict, total=False):
    owner: Required[str]

    language: Required[CodeScanningVariantAnalysisLanguage]
    """The language targeted by the CodeQL query"""

    query_pack: Required[str]
    """A Base64-encoded tarball containing a CodeQL query and all its dependencies"""

    repositories: list[str]
    """
    List of repository names (in the form `owner/repo-name`) to run the query
    against. Precisely one property from `repositories`, `repository_lists` and
    `repository_owners` is required.
    """

    repository_lists: list[str]
    """List of repository lists to run the query against.

    Precisely one property from `repositories`, `repository_lists` and
    `repository_owners` is required.
    """

    repository_owners: list[str]
    """
    List of organization or user names whose repositories the query should be run
    against. Precisely one property from `repositories`, `repository_lists` and
    `repository_owners` is required.
    """
