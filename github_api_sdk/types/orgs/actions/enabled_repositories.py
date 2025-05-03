

from typing_extensions import Literal, TypeAlias

__all__ = ["EnabledRepositories"]

EnabledRepositories: TypeAlias = Literal["all", "none", "selected"]
