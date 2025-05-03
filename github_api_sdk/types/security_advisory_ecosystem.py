

from typing_extensions import Literal, TypeAlias

__all__ = ["SecurityAdvisoryEcosystem"]

SecurityAdvisoryEcosystem: TypeAlias = Literal[
    "rubygems", "npm", "pip", "maven", "nuget", "composer", "go", "rust", "erlang", "actions", "pub", "other", "swift"
]
