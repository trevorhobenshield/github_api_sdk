

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CodespaceListDevcontainersResponse", "Devcontainer"]


class Devcontainer(BaseModel):
    path: str

    display_name: Optional[str] = None

    name: Optional[str] = None


class CodespaceListDevcontainersResponse(BaseModel):
    devcontainers: List[Devcontainer]

    total_count: int
