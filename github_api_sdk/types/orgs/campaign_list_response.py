

from typing import List
from typing_extensions import TypeAlias

from .summary import Summary

__all__ = ["CampaignListResponse"]

CampaignListResponse: TypeAlias = List[Summary]
