from __future__ import annotations

import httpx
from typing_extensions import Literal

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
from ...types.orgs import secret_scanning_list_alerts_params
from ...types.orgs.secret_scanning_list_alerts_response import SecretScanningListAlertsResponse

__all__ = ["SecretScanningResource", "AsyncSecretScanningResource"]


class SecretScanningResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecretScanningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SecretScanningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecretScanningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SecretScanningResourceWithStreamingResponse(self)

    def list_alerts(
        self,
        org: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        is_multi_repo: bool | NotGiven = NOT_GIVEN,
        is_publicly_leaked: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        resolution: str | NotGiven = NOT_GIVEN,
        secret_type: str | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "resolved"] | NotGiven = NOT_GIVEN,
        validity: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretScanningListAlertsResponse:
        """
        Lists secret scanning alerts for eligible repositories in an organization, from
        newest to oldest.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `security_events` scope to use this endpoint. If this endpoint is only used with
        public repositories, the token can use the `public_repo` scope instead.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for events after this cursor. To receive
              an initial cursor on your first request, include an empty "after" query string.

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for events before this cursor. To receive
              an initial cursor on your first request, include an empty "before" query string.

          direction: The direction to sort the results by.

          is_multi_repo: A boolean value representing whether or not to filter alerts by the multi-repo
              tag being present.

          is_publicly_leaked: A boolean value representing whether or not to filter alerts by the
              publicly-leaked tag being present.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          resolution: A comma-separated list of resolutions. Only secret scanning alerts with one of
              these resolutions are listed. Valid resolutions are `false_positive`,
              `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`.

          secret_type: A comma-separated list of secret types to return. All default secret patterns
              are returned. To return generic patterns, pass the token name(s) in the
              parameter. See
              "[Supported secret scanning patterns](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)"
              for a complete list of secret types.

          sort: The property to sort the results by. `created` means when the alert was created.
              `updated` means when the alert was updated or resolved.

          state: Set to `open` or `resolved` to only list secret scanning alerts in a specific
              state.

          validity: A comma-separated list of validities that, when present, will return alerts that
              match the validities in this list. Valid options are `active`, `inactive`, and
              `unknown`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/secret-scanning/alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "is_multi_repo": is_multi_repo,
                        "is_publicly_leaked": is_publicly_leaked,
                        "page": page,
                        "per_page": per_page,
                        "resolution": resolution,
                        "secret_type": secret_type,
                        "sort": sort,
                        "state": state,
                        "validity": validity,
                    },
                    secret_scanning_list_alerts_params.SecretScanningListAlertsParams,
                ),
            ),
            cast_to=SecretScanningListAlertsResponse,
        )


class AsyncSecretScanningResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecretScanningResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecretScanningResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecretScanningResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSecretScanningResourceWithStreamingResponse(self)

    async def list_alerts(
        self,
        org: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        is_multi_repo: bool | NotGiven = NOT_GIVEN,
        is_publicly_leaked: bool | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        resolution: str | NotGiven = NOT_GIVEN,
        secret_type: str | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "resolved"] | NotGiven = NOT_GIVEN,
        validity: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SecretScanningListAlertsResponse:
        """
        Lists secret scanning alerts for eligible repositories in an organization, from
        newest to oldest.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` or
        `security_events` scope to use this endpoint. If this endpoint is only used with
        public repositories, the token can use the `public_repo` scope instead.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for events after this cursor. To receive
              an initial cursor on your first request, include an empty "after" query string.

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for events before this cursor. To receive
              an initial cursor on your first request, include an empty "before" query string.

          direction: The direction to sort the results by.

          is_multi_repo: A boolean value representing whether or not to filter alerts by the multi-repo
              tag being present.

          is_publicly_leaked: A boolean value representing whether or not to filter alerts by the
              publicly-leaked tag being present.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          resolution: A comma-separated list of resolutions. Only secret scanning alerts with one of
              these resolutions are listed. Valid resolutions are `false_positive`,
              `wont_fix`, `revoked`, `pattern_edited`, `pattern_deleted` or `used_in_tests`.

          secret_type: A comma-separated list of secret types to return. All default secret patterns
              are returned. To return generic patterns, pass the token name(s) in the
              parameter. See
              "[Supported secret scanning patterns](https://docs.github.com/enterprise-cloud@latest/code-security/secret-scanning/introduction/supported-secret-scanning-patterns#supported-secrets)"
              for a complete list of secret types.

          sort: The property to sort the results by. `created` means when the alert was created.
              `updated` means when the alert was updated or resolved.

          state: Set to `open` or `resolved` to only list secret scanning alerts in a specific
              state.

          validity: A comma-separated list of validities that, when present, will return alerts that
              match the validities in this list. Valid options are `active`, `inactive`, and
              `unknown`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/secret-scanning/alerts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "direction": direction,
                        "is_multi_repo": is_multi_repo,
                        "is_publicly_leaked": is_publicly_leaked,
                        "page": page,
                        "per_page": per_page,
                        "resolution": resolution,
                        "secret_type": secret_type,
                        "sort": sort,
                        "state": state,
                        "validity": validity,
                    },
                    secret_scanning_list_alerts_params.SecretScanningListAlertsParams,
                ),
            ),
            cast_to=SecretScanningListAlertsResponse,
        )


class SecretScanningResourceWithRawResponse:
    def __init__(self, secret_scanning: SecretScanningResource) -> None:
        self._secret_scanning = secret_scanning

        self.list_alerts = to_raw_response_wrapper(
            secret_scanning.list_alerts,
        )


class AsyncSecretScanningResourceWithRawResponse:
    def __init__(self, secret_scanning: AsyncSecretScanningResource) -> None:
        self._secret_scanning = secret_scanning

        self.list_alerts = async_to_raw_response_wrapper(
            secret_scanning.list_alerts,
        )


class SecretScanningResourceWithStreamingResponse:
    def __init__(self, secret_scanning: SecretScanningResource) -> None:
        self._secret_scanning = secret_scanning

        self.list_alerts = to_streamed_response_wrapper(
            secret_scanning.list_alerts,
        )


class AsyncSecretScanningResourceWithStreamingResponse:
    def __init__(self, secret_scanning: AsyncSecretScanningResource) -> None:
        self._secret_scanning = secret_scanning

        self.list_alerts = async_to_streamed_response_wrapper(
            secret_scanning.list_alerts,
        )
