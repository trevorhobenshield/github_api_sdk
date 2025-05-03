

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["BillingGetUsageReportResponse", "UsageItem"]


class UsageItem(BaseModel):
    date: str
    """Date of the usage line item."""

    discount_amount: float = FieldInfo(alias="discountAmount")
    """Discount amount of the usage line item."""

    gross_amount: float = FieldInfo(alias="grossAmount")
    """Gross amount of the usage line item."""

    net_amount: float = FieldInfo(alias="netAmount")
    """Net amount of the usage line item."""

    organization_name: str = FieldInfo(alias="organizationName")
    """Name of the organization."""

    price_per_unit: float = FieldInfo(alias="pricePerUnit")
    """Price per unit of the usage line item."""

    product: str
    """Product name."""

    quantity: int
    """Quantity of the usage line item."""

    sku: str
    """SKU name."""

    unit_type: str = FieldInfo(alias="unitType")
    """Unit type of the usage line item."""

    repository_name: Optional[str] = FieldInfo(alias="repositoryName", default=None)
    """Name of the repository."""


class BillingGetUsageReportResponse(BaseModel):
    usage_items: Optional[List[UsageItem]] = FieldInfo(alias="usageItems", default=None)
