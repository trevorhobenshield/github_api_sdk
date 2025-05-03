


from ....._models import BaseModel

__all__ = ["ProtectedBranchAdminEnforced"]


class ProtectedBranchAdminEnforced(BaseModel):
    enabled: bool

    url: str
