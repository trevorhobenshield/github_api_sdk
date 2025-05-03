

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["GpgKey", "Email", "Subkey", "SubkeyEmail"]


class Email(BaseModel):
    email: Optional[str] = None

    verified: Optional[bool] = None


class SubkeyEmail(BaseModel):
    email: Optional[str] = None

    verified: Optional[bool] = None


class Subkey(BaseModel):
    id: Optional[int] = None

    can_certify: Optional[bool] = None

    can_encrypt_comms: Optional[bool] = None

    can_encrypt_storage: Optional[bool] = None

    can_sign: Optional[bool] = None

    created_at: Optional[str] = None

    emails: Optional[List[SubkeyEmail]] = None

    expires_at: Optional[str] = None

    key_id: Optional[str] = None

    primary_key_id: Optional[int] = None

    public_key: Optional[str] = None

    raw_key: Optional[str] = None

    revoked: Optional[bool] = None

    subkeys: Optional[List[object]] = None


class GpgKey(BaseModel):
    id: int

    can_certify: bool

    can_encrypt_comms: bool

    can_encrypt_storage: bool

    can_sign: bool

    created_at: datetime

    emails: List[Email]

    expires_at: Optional[datetime] = None

    key_id: str

    primary_key_id: Optional[int] = None

    public_key: str

    raw_key: Optional[str] = None

    revoked: bool

    subkeys: List[Subkey]

    name: Optional[str] = None
