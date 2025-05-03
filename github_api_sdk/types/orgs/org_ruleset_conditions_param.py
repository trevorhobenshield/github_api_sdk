

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from ..repos.repository_ruleset_conditions_param import RepositoryRulesetConditionsParam
from .repository_ruleset_conditions_repository_property_spec_param import (
    RepositoryRulesetConditionsRepositoryPropertySpecParam,
)

__all__ = [
    "OrgRulesetConditionsParam",
    "RepositoryNameAndRefName",
    "RepositoryNameAndRefNameRepositoryName",
    "RepositoryIDAndRefName",
    "RepositoryIDAndRefNameRepositoryID",
    "RepositoryPropertyAndRefName",
    "RepositoryPropertyAndRefNameRepositoryProperty",
]


class RepositoryNameAndRefNameRepositoryName(TypedDict, total=False):
    exclude: list[str]
    """Array of repository names or patterns to exclude.

    The condition will not pass if any of these patterns match.
    """

    include: list[str]
    """Array of repository names or patterns to include.

    One of these patterns must match for the condition to pass. Also accepts `~ALL`
    to include all repositories.
    """

    protected: bool
    """Whether renaming of target repositories is prevented."""


class RepositoryNameAndRefName(RepositoryRulesetConditionsParam, total=False):
    repository_name: Required[RepositoryNameAndRefNameRepositoryName]


class RepositoryIDAndRefNameRepositoryID(TypedDict, total=False):
    repository_ids: Iterable[int]
    """The repository IDs that the ruleset applies to.

    One of these IDs must match for the condition to pass.
    """


class RepositoryIDAndRefName(RepositoryRulesetConditionsParam, total=False):
    repository_id: Required[RepositoryIDAndRefNameRepositoryID]


class RepositoryPropertyAndRefNameRepositoryProperty(TypedDict, total=False):
    exclude: Iterable[RepositoryRulesetConditionsRepositoryPropertySpecParam]
    """The repository properties and values to exclude.

    The condition will not pass if any of these properties match.
    """

    include: Iterable[RepositoryRulesetConditionsRepositoryPropertySpecParam]
    """The repository properties and values to include.

    All of these properties must match for the condition to pass.
    """


class RepositoryPropertyAndRefName(RepositoryRulesetConditionsParam, total=False):
    repository_property: Required[RepositoryPropertyAndRefNameRepositoryProperty]


OrgRulesetConditionsParam: TypeAlias = Union[
    RepositoryNameAndRefName, RepositoryIDAndRefName, RepositoryPropertyAndRefName
]
