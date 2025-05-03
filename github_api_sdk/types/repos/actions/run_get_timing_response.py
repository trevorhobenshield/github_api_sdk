

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "RunGetTimingResponse",
    "Billable",
    "BillableMacos",
    "BillableMacosJobRun",
    "BillableUbuntu",
    "BillableUbuntuJobRun",
    "BillableWindows",
    "BillableWindowsJobRun",
]


class BillableMacosJobRun(BaseModel):
    duration_ms: int

    job_id: int


class BillableMacos(BaseModel):
    jobs: int

    total_ms: int

    job_runs: Optional[List[BillableMacosJobRun]] = None


class BillableUbuntuJobRun(BaseModel):
    duration_ms: int

    job_id: int


class BillableUbuntu(BaseModel):
    jobs: int

    total_ms: int

    job_runs: Optional[List[BillableUbuntuJobRun]] = None


class BillableWindowsJobRun(BaseModel):
    duration_ms: int

    job_id: int


class BillableWindows(BaseModel):
    jobs: int

    total_ms: int

    job_runs: Optional[List[BillableWindowsJobRun]] = None


class Billable(BaseModel):
    macos: Optional[BillableMacos] = FieldInfo(alias="MACOS", default=None)

    ubuntu: Optional[BillableUbuntu] = FieldInfo(alias="UBUNTU", default=None)

    windows: Optional[BillableWindows] = FieldInfo(alias="WINDOWS", default=None)


class RunGetTimingResponse(BaseModel):
    billable: Billable

    run_duration_ms: Optional[int] = None
