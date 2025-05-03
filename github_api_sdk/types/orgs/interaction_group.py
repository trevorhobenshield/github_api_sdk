

from typing_extensions import Literal, TypeAlias

__all__ = ["InteractionGroup"]

InteractionGroup: TypeAlias = Literal["existing_users", "contributors_only", "collaborators_only"]
