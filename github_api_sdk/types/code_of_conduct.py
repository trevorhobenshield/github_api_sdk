

from typing import Optional

from .._models import BaseModel

__all__ = ["CodeOfConduct"]


class CodeOfConduct(BaseModel):
    html_url: Optional[str] = None

    key: str

    name: str

    url: str

    body: Optional[str] = None
