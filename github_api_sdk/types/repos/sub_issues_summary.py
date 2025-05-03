


from ..._models import BaseModel

__all__ = ["SubIssuesSummary"]


class SubIssuesSummary(BaseModel):
    completed: int

    percent_completed: int

    total: int
