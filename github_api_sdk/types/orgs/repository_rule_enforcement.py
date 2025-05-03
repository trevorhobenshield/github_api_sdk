

from typing_extensions import Literal, TypeAlias

__all__ = ["RepositoryRuleEnforcement"]

RepositoryRuleEnforcement: TypeAlias = Literal["disabled", "active", "evaluate"]
