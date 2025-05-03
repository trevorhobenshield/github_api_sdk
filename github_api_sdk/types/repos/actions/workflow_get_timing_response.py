

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["WorkflowGetTimingResponse", "Billable", "BillableMacos", "BillableUbuntu", "BillableWindows"]


class BillableMacos(BaseModel):
    total_ms: Optional[int] = None


class BillableUbuntu(BaseModel):
    total_ms: Optional[int] = None


class BillableWindows(BaseModel):
    total_ms: Optional[int] = None


class Billable(BaseModel):
    macos: Optional[BillableMacos] = FieldInfo(alias="MACOS", default=None)

    ubuntu: Optional[BillableUbuntu] = FieldInfo(alias="UBUNTU", default=None)

    windows: Optional[BillableWindows] = FieldInfo(alias="WINDOWS", default=None)


class WorkflowGetTimingResponse(BaseModel):
    billable: Billable
