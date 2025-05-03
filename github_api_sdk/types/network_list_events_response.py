

from typing import List
from typing_extensions import TypeAlias

from .event import Event

__all__ = ["NetworkListEventsResponse"]

NetworkListEventsResponse: TypeAlias = List[Event]
