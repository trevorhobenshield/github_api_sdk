

from typing import List

from ...._models import BaseModel
from .machine_spec import MachineSpec

__all__ = ["HostedRunnerGetMachineSizesResponse"]


class HostedRunnerGetMachineSizesResponse(BaseModel):
    machine_specs: List[MachineSpec]

    total_count: int
