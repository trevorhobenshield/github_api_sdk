

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "MetaRetrieveResponse",
    "Domains",
    "DomainsActionsInbound",
    "DomainsArtifactAttestations",
    "SSHKeyFingerprints",
]


class DomainsActionsInbound(BaseModel):
    full_domains: Optional[List[str]] = None

    wildcard_domains: Optional[List[str]] = None


class DomainsArtifactAttestations(BaseModel):
    services: Optional[List[str]] = None

    trust_domain: Optional[str] = None


class Domains(BaseModel):
    actions: Optional[List[str]] = None

    actions_inbound: Optional[DomainsActionsInbound] = None

    artifact_attestations: Optional[DomainsArtifactAttestations] = None

    codespaces: Optional[List[str]] = None

    copilot: Optional[List[str]] = None

    packages: Optional[List[str]] = None

    website: Optional[List[str]] = None


class SSHKeyFingerprints(BaseModel):
    sha256_dsa: Optional[str] = FieldInfo(alias="SHA256_DSA", default=None)

    sha256_ecdsa: Optional[str] = FieldInfo(alias="SHA256_ECDSA", default=None)

    sha256_ed25519: Optional[str] = FieldInfo(alias="SHA256_ED25519", default=None)

    sha256_rsa: Optional[str] = FieldInfo(alias="SHA256_RSA", default=None)


class MetaRetrieveResponse(BaseModel):
    verifiable_password_authentication: bool

    actions: Optional[List[str]] = None

    actions_macos: Optional[List[str]] = None

    api: Optional[List[str]] = None

    codespaces: Optional[List[str]] = None

    copilot: Optional[List[str]] = None

    dependabot: Optional[List[str]] = None

    domains: Optional[Domains] = None

    git: Optional[List[str]] = None

    github_enterprise_importer: Optional[List[str]] = None

    hooks: Optional[List[str]] = None

    importer: Optional[List[str]] = None

    packages: Optional[List[str]] = None

    pages: Optional[List[str]] = None

    ssh_key_fingerprints: Optional[SSHKeyFingerprints] = None

    ssh_keys: Optional[List[str]] = None

    web: Optional[List[str]] = None
