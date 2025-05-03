

from typing import List
from typing_extensions import TypeAlias

from .release_asset import ReleaseAsset

__all__ = ["AssetListResponse"]

AssetListResponse: TypeAlias = List[ReleaseAsset]
