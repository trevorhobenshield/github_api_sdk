

from typing_extensions import Literal, TypeAlias

__all__ = ["AllowedActions"]

AllowedActions: TypeAlias = Literal["all", "local_only", "selected"]
