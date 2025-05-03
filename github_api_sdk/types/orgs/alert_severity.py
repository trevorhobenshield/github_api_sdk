

from typing_extensions import Literal, TypeAlias

__all__ = ["AlertSeverity"]

AlertSeverity: TypeAlias = Literal["critical", "high", "medium", "low", "warning", "note", "error"]
