

from typing import List
from typing_extensions import TypeAlias

from .users.ssh_signing_key import SSHSigningKey

__all__ = ["UserListSSHSigningKeysResponse"]

UserListSSHSigningKeysResponse: TypeAlias = List[SSHSigningKey]
