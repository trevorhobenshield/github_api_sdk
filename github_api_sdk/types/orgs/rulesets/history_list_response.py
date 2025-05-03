

from typing import List
from typing_extensions import TypeAlias

from .ruleset_version import RulesetVersion

__all__ = ["HistoryListResponse"]

HistoryListResponse: TypeAlias = List[RulesetVersion]
