


from ..._models import BaseModel

__all__ = ["CodespaceCheckPermissionsResponse"]


class CodespaceCheckPermissionsResponse(BaseModel):
    accepted: bool
    """
    Whether the user has accepted the permissions defined by the devcontainer config
    """
