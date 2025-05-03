

from typing import TYPE_CHECKING, Optional

from .integration import Integration

__all__ = ["AppManifestCreateConversionResponse"]


class AppManifestCreateConversionResponse(Integration):
    client_id: str  # type: ignore

    client_secret: str  # type: ignore

    pem: str  # type: ignore

    webhook_secret: Optional[str] = None  # type: ignore

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
