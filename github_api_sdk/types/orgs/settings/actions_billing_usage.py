

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ActionsBillingUsage", "MinutesUsedBreakdown"]


class MinutesUsedBreakdown(BaseModel):
    macos: Optional[int] = FieldInfo(alias="MACOS", default=None)
    """Total minutes used on macOS runner machines."""

    macos_12_core: Optional[int] = None
    """Total minutes used on macOS 12 core runner machines."""

    total: Optional[int] = None
    """Total minutes used on all runner machines."""

    ubuntu: Optional[int] = FieldInfo(alias="UBUNTU", default=None)
    """Total minutes used on Ubuntu runner machines."""

    ubuntu_16_core: Optional[int] = None
    """Total minutes used on Ubuntu 16 core runner machines."""

    ubuntu_32_core: Optional[int] = None
    """Total minutes used on Ubuntu 32 core runner machines."""

    ubuntu_4_core: Optional[int] = None
    """Total minutes used on Ubuntu 4 core runner machines."""

    ubuntu_64_core: Optional[int] = None
    """Total minutes used on Ubuntu 64 core runner machines."""

    ubuntu_8_core: Optional[int] = None
    """Total minutes used on Ubuntu 8 core runner machines."""

    windows: Optional[int] = FieldInfo(alias="WINDOWS", default=None)
    """Total minutes used on Windows runner machines."""

    windows_16_core: Optional[int] = None
    """Total minutes used on Windows 16 core runner machines."""

    windows_32_core: Optional[int] = None
    """Total minutes used on Windows 32 core runner machines."""

    windows_4_core: Optional[int] = None
    """Total minutes used on Windows 4 core runner machines."""

    windows_64_core: Optional[int] = None
    """Total minutes used on Windows 64 core runner machines."""

    windows_8_core: Optional[int] = None
    """Total minutes used on Windows 8 core runner machines."""


class ActionsBillingUsage(BaseModel):
    included_minutes: int
    """The amount of free GitHub Actions minutes available."""

    minutes_used_breakdown: MinutesUsedBreakdown

    total_minutes_used: int
    """The sum of the free and paid GitHub Actions minutes used."""

    total_paid_minutes_used: int
    """The total paid GitHub Actions minutes used."""
