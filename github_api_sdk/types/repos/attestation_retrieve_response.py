

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AttestationRetrieveResponse", "Attestation", "AttestationBundle"]


class AttestationBundle(BaseModel):
    dsse_envelope: Optional[Dict[str, object]] = FieldInfo(alias="dsseEnvelope", default=None)

    media_type: Optional[str] = FieldInfo(alias="mediaType", default=None)

    verification_material: Optional[Dict[str, object]] = FieldInfo(alias="verificationMaterial", default=None)


class Attestation(BaseModel):
    bundle: Optional[AttestationBundle] = None
    """
    The attestation's Sigstore Bundle. Refer to the
    [Sigstore Bundle Specification](https://github.com/sigstore/protobuf-specs/blob/main/protos/sigstore_bundle.proto)
    for more information.
    """

    bundle_url: Optional[str] = None

    repository_id: Optional[int] = None


class AttestationRetrieveResponse(BaseModel):
    attestations: Optional[List[Attestation]] = None
