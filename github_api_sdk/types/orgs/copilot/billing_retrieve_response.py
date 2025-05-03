

from typing import TYPE_CHECKING, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BillingRetrieveResponse", "SeatBreakdown"]


class SeatBreakdown(BaseModel):
    active_this_cycle: Optional[int] = None
    """The number of seats that have used Copilot during the current billing cycle."""

    added_this_cycle: Optional[int] = None
    """Seats added during the current billing cycle."""

    inactive_this_cycle: Optional[int] = None
    """
    The number of seats that have not used Copilot during the current billing cycle.
    """

    pending_cancellation: Optional[int] = None
    """
    The number of seats that are pending cancellation at the end of the current
    billing cycle.
    """

    pending_invitation: Optional[int] = None
    """
    The number of users who have been invited to receive a Copilot seat through this
    organization.
    """

    total: Optional[int] = None
    """
    The total number of seats being billed for the organization as of the current
    billing cycle.
    """


class BillingRetrieveResponse(BaseModel):
    public_code_suggestions: Literal["allow", "block", "unconfigured"]
    """
    The organization policy for allowing or blocking suggestions matching public
    code (duplication detection filter).
    """

    seat_breakdown: SeatBreakdown
    """The breakdown of Copilot Business seats for the organization."""

    seat_management_setting: Literal["assign_all", "assign_selected", "disabled", "unconfigured"]
    """The mode of assigning new seats."""

    cli: Optional[Literal["enabled", "disabled", "unconfigured"]] = None
    """The organization policy for allowing or disallowing Copilot in the CLI."""

    ide_chat: Optional[Literal["enabled", "disabled", "unconfigured"]] = None
    """The organization policy for allowing or disallowing Copilot Chat in the IDE."""

    plan_type: Optional[Literal["business", "enterprise"]] = None
    """
    The Copilot plan of the organization, or the parent enterprise, when applicable.
    """

    platform_chat: Optional[Literal["enabled", "disabled", "unconfigured"]] = None
    """
    The organization policy for allowing or disallowing Copilot features on
    GitHub.com.
    """

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
