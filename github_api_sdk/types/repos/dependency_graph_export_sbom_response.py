

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "DependencyGraphExportSbomResponse",
    "Sbom",
    "SbomCreationInfo",
    "SbomPackage",
    "SbomPackageExternalRef",
    "SbomRelationship",
]


class SbomCreationInfo(BaseModel):
    created: str
    """The date and time the SPDX document was created."""

    creators: List[str]
    """The tools that were used to generate the SPDX document."""


class SbomPackageExternalRef(BaseModel):
    reference_category: str = FieldInfo(alias="referenceCategory")
    """The category of reference to an external resource this reference refers to."""

    reference_locator: str = FieldInfo(alias="referenceLocator")
    """A locator for the particular external resource this reference refers to."""

    reference_type: str = FieldInfo(alias="referenceType")
    """The category of reference to an external resource this reference refers to."""


class SbomPackage(BaseModel):
    copyright_text: Optional[str] = FieldInfo(alias="copyrightText", default=None)
    """
    The copyright holders of the package, and any dates present with those notices,
    if available.
    """

    download_location: Optional[str] = FieldInfo(alias="downloadLocation", default=None)
    """
    The location where the package can be downloaded, or NOASSERTION if this has not
    been determined.
    """

    external_refs: Optional[List[SbomPackageExternalRef]] = FieldInfo(alias="externalRefs", default=None)

    files_analyzed: Optional[bool] = FieldInfo(alias="filesAnalyzed", default=None)
    """
    Whether the package's file content has been subjected to analysis during the
    creation of the SPDX document.
    """

    license_concluded: Optional[str] = FieldInfo(alias="licenseConcluded", default=None)
    """The license of the package as determined while creating the SPDX document."""

    license_declared: Optional[str] = FieldInfo(alias="licenseDeclared", default=None)
    """
    The license of the package as declared by its author, or NOASSERTION if this
    information was not available when the SPDX document was created.
    """

    name: Optional[str] = None
    """The name of the package."""

    spdxid: Optional[str] = FieldInfo(alias="SPDXID", default=None)
    """A unique SPDX identifier for the package."""

    supplier: Optional[str] = None
    """
    The distribution source of this package, or NOASSERTION if this was not
    determined.
    """

    version_info: Optional[str] = FieldInfo(alias="versionInfo", default=None)
    """The version of the package.

    If the package does not have an exact version specified, a version range is
    given.
    """


class SbomRelationship(BaseModel):
    related_spdx_element: Optional[str] = FieldInfo(alias="relatedSpdxElement", default=None)
    """The SPDX identifier of the package that is the target of the relationship."""

    relationship_type: Optional[str] = FieldInfo(alias="relationshipType", default=None)
    """The type of relationship between the two SPDX elements."""

    spdx_element_id: Optional[str] = FieldInfo(alias="spdxElementId", default=None)
    """The SPDX identifier of the package that is the source of the relationship."""


class Sbom(BaseModel):
    creation_info: SbomCreationInfo = FieldInfo(alias="creationInfo")

    data_license: str = FieldInfo(alias="dataLicense")
    """The license under which the SPDX document is licensed."""

    document_namespace: str = FieldInfo(alias="documentNamespace")
    """The namespace for the SPDX document."""

    name: str
    """The name of the SPDX document."""

    packages: List[SbomPackage]

    spdxid: str = FieldInfo(alias="SPDXID")
    """The SPDX identifier for the SPDX document."""

    spdx_version: str = FieldInfo(alias="spdxVersion")
    """The version of the SPDX specification that this document conforms to."""

    comment: Optional[str] = None
    """An optional comment about the SPDX document."""

    relationships: Optional[List[SbomRelationship]] = None


class DependencyGraphExportSbomResponse(BaseModel):
    sbom: Sbom
