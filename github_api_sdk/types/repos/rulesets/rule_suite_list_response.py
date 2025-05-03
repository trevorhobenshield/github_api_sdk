

from typing import List
from typing_extensions import TypeAlias

from ...orgs.rulesets.items import Items

__all__ = ["RuleSuiteListResponse"]

RuleSuiteListResponse: TypeAlias = List[Items]
