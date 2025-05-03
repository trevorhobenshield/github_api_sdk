

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AttestationCreateParams", "Bundle"]


class AttestationCreateParams(TypedDict, total=False):
    owner: Required[str]

    bundle: Required[Bundle]
    """
    The attestation's Sigstore Bundle. Refer to the
    [Sigstore Bundle Specification](https://github.com/sigstore/protobuf-specs/blob/main/protos/sigstore_bundle.proto)
    for more information.
    """


class Bundle(TypedDict, total=False):
    dsse_envelope: Annotated[dict[str, object], PropertyInfo(alias="dsseEnvelope")]

    media_type: Annotated[str, PropertyInfo(alias="mediaType")]

    verification_material: Annotated[dict[str, object], PropertyInfo(alias="verificationMaterial")]
