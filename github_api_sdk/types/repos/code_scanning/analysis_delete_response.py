

from typing import Optional

from ...._models import BaseModel

__all__ = ["AnalysisDeleteResponse"]


class AnalysisDeleteResponse(BaseModel):
    confirm_delete_url: Optional[str] = None
    """Next deletable analysis in chain, with last analysis deletion confirmation"""

    next_analysis_url: Optional[str] = None
    """Next deletable analysis in chain, without last analysis deletion confirmation"""
