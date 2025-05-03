

from typing import Optional

from ...._models import BaseModel

__all__ = ["Application"]


class Application(BaseModel):
    architecture: str

    download_url: str

    filename: str

    os: str

    sha256_checksum: Optional[str] = None

    temp_download_token: Optional[str] = None
    """A short lived bearer token used to download the runner, if needed."""
