from __future__ import annotations

import httpx

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.repos import attestation_create_params, attestation_retrieve_params
from ...types.repos.attestation_create_response import AttestationCreateResponse
from ...types.repos.attestation_retrieve_response import AttestationRetrieveResponse

__all__ = ["AttestationsResource", "AsyncAttestationsResource"]


class AttestationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttestationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AttestationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttestationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AttestationsResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        bundle: attestation_create_params.Bundle,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttestationCreateResponse:
        """
        Store an artifact attestation and associate it with a repository.

        The authenticated user must have write permission to the repository and, if
        using a fine-grained access token, the `attestations:write` permission is
        required.

        Artifact attestations are meant to be created using the
        [attest action](https://github.com/actions/attest). For more information, see
        our guide on
        [using artifact attestations to establish a build's provenance](https://docs.github.com/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds).

        Args:
          bundle: The attestation's Sigstore Bundle. Refer to the
              [Sigstore Bundle Specification](https://github.com/sigstore/protobuf-specs/blob/main/protos/sigstore_bundle.proto)
              for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/attestations",
            body=maybe_transform({"bundle": bundle}, attestation_create_params.AttestationCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AttestationCreateResponse,
        )

    def retrieve(
        self,
        subject_digest: str,
        *,
        owner: str,
        repo: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        predicate_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttestationRetrieveResponse:
        """
        List a collection of artifact attestations with a given subject digest that are
        associated with a repository.

        The authenticated user making the request must have read access to the
        repository. In addition, when using a fine-grained access token the
        `attestations:read` permission is required.

        **Please note:** in order to offer meaningful security benefits, an
        attestation's signature and timestamps **must** be cryptographically verified,
        and the identity of the attestation signer **must** be validated. Attestations
        can be verified using the
        [GitHub CLI `attestation verify` command](https://cli.github.com/manual/gh_attestation_verify).
        For more information, see
        [our guide on how to use artifact attestations to establish a build's provenance](https://docs.github.com/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds).

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          predicate_type: Optional filter for fetching attestations with a given predicate type. This
              option accepts `provenance`, `sbom`, or freeform text for custom predicate
              types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not subject_digest:
            raise ValueError(f"Expected a non-empty value for `subject_digest` but received {subject_digest!r}")
        return self._get(
            f"/repos/{owner}/{repo}/attestations/{subject_digest}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "per_page": per_page,
                        "predicate_type": predicate_type,
                    },
                    attestation_retrieve_params.AttestationRetrieveParams,
                ),
            ),
            cast_to=AttestationRetrieveResponse,
        )


class AsyncAttestationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttestationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAttestationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttestationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAttestationsResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        bundle: attestation_create_params.Bundle,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttestationCreateResponse:
        """
        Store an artifact attestation and associate it with a repository.

        The authenticated user must have write permission to the repository and, if
        using a fine-grained access token, the `attestations:write` permission is
        required.

        Artifact attestations are meant to be created using the
        [attest action](https://github.com/actions/attest). For more information, see
        our guide on
        [using artifact attestations to establish a build's provenance](https://docs.github.com/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds).

        Args:
          bundle: The attestation's Sigstore Bundle. Refer to the
              [Sigstore Bundle Specification](https://github.com/sigstore/protobuf-specs/blob/main/protos/sigstore_bundle.proto)
              for more information.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/attestations",
            body=await async_maybe_transform({"bundle": bundle}, attestation_create_params.AttestationCreateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AttestationCreateResponse,
        )

    async def retrieve(
        self,
        subject_digest: str,
        *,
        owner: str,
        repo: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        predicate_type: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AttestationRetrieveResponse:
        """
        List a collection of artifact attestations with a given subject digest that are
        associated with a repository.

        The authenticated user making the request must have read access to the
        repository. In addition, when using a fine-grained access token the
        `attestations:read` permission is required.

        **Please note:** in order to offer meaningful security benefits, an
        attestation's signature and timestamps **must** be cryptographically verified,
        and the identity of the attestation signer **must** be validated. Attestations
        can be verified using the
        [GitHub CLI `attestation verify` command](https://cli.github.com/manual/gh_attestation_verify).
        For more information, see
        [our guide on how to use artifact attestations to establish a build's provenance](https://docs.github.com/actions/security-guides/using-artifact-attestations-to-establish-provenance-for-builds).

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          predicate_type: Optional filter for fetching attestations with a given predicate type. This
              option accepts `provenance`, `sbom`, or freeform text for custom predicate
              types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not subject_digest:
            raise ValueError(f"Expected a non-empty value for `subject_digest` but received {subject_digest!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/attestations/{subject_digest}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "per_page": per_page,
                        "predicate_type": predicate_type,
                    },
                    attestation_retrieve_params.AttestationRetrieveParams,
                ),
            ),
            cast_to=AttestationRetrieveResponse,
        )


class AttestationsResourceWithRawResponse:
    def __init__(self, attestations: AttestationsResource) -> None:
        self._attestations = attestations

        self.create = to_raw_response_wrapper(
            attestations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            attestations.retrieve,
        )


class AsyncAttestationsResourceWithRawResponse:
    def __init__(self, attestations: AsyncAttestationsResource) -> None:
        self._attestations = attestations

        self.create = async_to_raw_response_wrapper(
            attestations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            attestations.retrieve,
        )


class AttestationsResourceWithStreamingResponse:
    def __init__(self, attestations: AttestationsResource) -> None:
        self._attestations = attestations

        self.create = to_streamed_response_wrapper(
            attestations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            attestations.retrieve,
        )


class AsyncAttestationsResourceWithStreamingResponse:
    def __init__(self, attestations: AsyncAttestationsResource) -> None:
        self._attestations = attestations

        self.create = async_to_streamed_response_wrapper(
            attestations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            attestations.retrieve,
        )
