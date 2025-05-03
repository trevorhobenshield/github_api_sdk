

from typing_extensions import Literal, TypeAlias

__all__ = ["AuthorAssociation"]

AuthorAssociation: TypeAlias = Literal[
    "COLLABORATOR", "CONTRIBUTOR", "FIRST_TIMER", "FIRST_TIME_CONTRIBUTOR", "MANNEQUIN", "MEMBER", "NONE", "OWNER"
]
