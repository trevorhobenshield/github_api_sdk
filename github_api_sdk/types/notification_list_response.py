

from typing import List
from typing_extensions import TypeAlias

from .notifications.thread import Thread

__all__ = ["NotificationListResponse"]

NotificationListResponse: TypeAlias = List[Thread]
