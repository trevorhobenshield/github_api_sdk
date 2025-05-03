

from typing import List
from typing_extensions import TypeAlias

from .ssh_signing_key import SSHSigningKey

__all__ = ["SSHSigningKeyListResponse"]

SSHSigningKeyListResponse: TypeAlias = List[SSHSigningKey]
