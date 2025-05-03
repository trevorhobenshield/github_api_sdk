

from typing import List
from typing_extensions import TypeAlias

from ...orgs.actions.application import Application

__all__ = ["RunnerListDownloadsResponse"]

RunnerListDownloadsResponse: TypeAlias = List[Application]
