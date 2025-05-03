

from typing_extensions import Literal, TypeAlias

__all__ = ["PushProtectionBypassReason"]

PushProtectionBypassReason: TypeAlias = Literal["false_positive", "used_in_tests", "will_fix_later"]
