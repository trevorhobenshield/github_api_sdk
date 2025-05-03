

from typing import List
from typing_extensions import TypeAlias

from .items import Items

__all__ = ["RuleSuiteListResponse"]

RuleSuiteListResponse: TypeAlias = List[Items]
