

from typing import Union
from typing_extensions import TypeAlias

from ..orgs.interaction_limit_response import InteractionLimitResponse

__all__ = ["InteractionLimitRetrieveResponse"]

InteractionLimitRetrieveResponse: TypeAlias = Union[InteractionLimitResponse, object]
