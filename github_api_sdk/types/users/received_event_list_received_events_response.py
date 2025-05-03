

from typing import TYPE_CHECKING, List
from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from ..event import Event

__all__ = ["ReceivedEventListReceivedEventsResponse"]

ReceivedEventListReceivedEventsResponse: TypeAlias = List["Event"]
