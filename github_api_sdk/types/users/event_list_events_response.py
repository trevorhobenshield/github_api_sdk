

from typing import TYPE_CHECKING, List
from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from ..event import Event

__all__ = ["EventListEventsResponse"]

EventListEventsResponse: TypeAlias = List["Event"]
