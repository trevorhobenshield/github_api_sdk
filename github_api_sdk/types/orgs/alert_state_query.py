

from typing_extensions import Literal, TypeAlias

__all__ = ["AlertStateQuery"]

AlertStateQuery: TypeAlias = Literal["open", "closed", "dismissed", "fixed"]
