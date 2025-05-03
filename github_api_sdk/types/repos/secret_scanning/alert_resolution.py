

from typing import Optional
from typing_extensions import Literal, TypeAlias

__all__ = ["AlertResolution"]

AlertResolution: TypeAlias = Optional[Literal["false_positive", "wont_fix", "revoked", "used_in_tests"]]
