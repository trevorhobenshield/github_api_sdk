

from typing import List
from typing_extensions import TypeAlias

from .repository_ruleset import RepositoryRuleset

__all__ = ["RulesetListResponse"]

RulesetListResponse: TypeAlias = List[RepositoryRuleset]
