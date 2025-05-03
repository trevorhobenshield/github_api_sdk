

from typing import Optional

from .._models import BaseModel

__all__ = ["CvssSeverity", "CvssV3", "CvssV4"]


class CvssV3(BaseModel):
    score: Optional[float] = None
    """The CVSS 3 score."""

    vector_string: Optional[str] = None
    """The CVSS 3 vector string."""


class CvssV4(BaseModel):
    score: Optional[float] = None
    """The CVSS 4 score."""

    vector_string: Optional[str] = None
    """The CVSS 4 vector string."""


class CvssSeverity(BaseModel):
    cvss_v3: Optional[CvssV3] = None

    cvss_v4: Optional[CvssV4] = None
