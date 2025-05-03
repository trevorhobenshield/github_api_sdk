


from ...._models import BaseModel

__all__ = ["MachineSpec"]


class MachineSpec(BaseModel):
    id: str
    """The ID used for the `size` parameter when creating a new runner."""

    cpu_cores: int
    """The number of cores."""

    memory_gb: int
    """The available RAM for the machine spec."""

    storage_gb: int
    """The available SSD storage for the machine spec."""
