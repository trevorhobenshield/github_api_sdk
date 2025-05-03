

from typing import List
from typing_extensions import TypeAlias

from ...orgs.rulesets.ruleset_version import RulesetVersion

__all__ = ["HistoryRetrieveResponse"]

HistoryRetrieveResponse: TypeAlias = List[RulesetVersion]
