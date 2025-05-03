from __future__ import annotations

import httpx

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, FileTypes, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.releases import asset_list_params, asset_update_params, asset_upload_params
from ....types.repos.releases.asset_list_response import AssetListResponse
from ....types.repos.releases.release_asset import ReleaseAsset

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AssetsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        asset_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseAsset:
        """
        To download the asset's binary content:

        - If within a browser, fetch the location specified in the
          `browser_download_url` key provided in the response.
        - Alternatively, set the `Accept` header of the request to
          [`application/octet-stream`](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).
          The API will either redirect the client to the location, or stream it directly
          if possible. API clients should handle both a `200` or `302` response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/releases/assets/{asset_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReleaseAsset,
        )

    def update(
        self,
        asset_id: int,
        *,
        owner: str,
        repo: str,
        label: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseAsset:
        """
        Users with push access to the repository can edit a release asset.

        Args:
          label: An alternate short description of the asset. Used in place of the filename.

          name: The file name of the asset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._patch(
            f"/repos/{owner}/{repo}/releases/assets/{asset_id}",
            body=maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "state": state,
                },
                asset_update_params.AssetUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReleaseAsset,
        )

    def list(
        self,
        release_id: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetListResponse:
        """List release assets

        Args:
          page: The page number of the results to fetch.

        For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/releases/{release_id}/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            cast_to=AssetListResponse,
        )

    def delete(
        self,
        asset_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a release asset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/releases/assets/{asset_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def upload(
        self,
        release_id: int,
        *,
        owner: str,
        repo: str,
        name: str,
        label: str | NotGiven = NOT_GIVEN,
        body: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseAsset:
        """
        This endpoint makes use of a
        [Hypermedia relation](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia)
        to determine which URL to access. The endpoint you call to upload release assets
        is specific to your release. Use the `upload_url` returned in the response of
        the
        [Create a release endpoint](https://docs.github.com/rest/releases/releases#create-a-release)
        to upload a release asset.

        You need to use an HTTP client which supports
        [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) to make calls to this
        endpoint.

        Most libraries will set the required `Content-Length` header automatically. Use
        the required `Content-Type` header to provide the media type of the asset. For a
        list of media types, see
        [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml).
        For example:

        `application/zip`

        GitHub expects the asset data in its raw binary form, rather than JSON. You will
        send the raw binary content of the asset as the request body. Everything else
        about the endpoint is the same as the rest of the API. For example, you'll still
        need to pass your authentication to be able to upload an asset.

        When an upstream failure occurs, you will receive a `502 Bad Gateway` status.
        This may leave an empty asset with a state of `starter`. It can be safely
        deleted.

        **Notes:**

        - GitHub renames asset filenames that have special characters, non-alphanumeric
          characters, and leading or trailing periods. The
          "[List release assets](https://docs.github.com/rest/releases/assets#list-release-assets)"
          endpoint lists the renamed filenames. For more information and help, contact
          [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api).
        - To find the `release_id` query the
          [`GET /repos/{owner}/{repo}/releases/latest` endpoint](https://docs.github.com/rest/releases/releases#get-the-latest-release).
        - If you upload an asset with the same filename as another uploaded asset,
          you'll receive an error and must delete the old file before you can re-upload
          the new asset.

        Args:
          body: The raw file data

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
            f"/repos/{owner}/{repo}/releases/{release_id}/assets",
            body=maybe_transform(body, asset_upload_params.AssetUploadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "label": label,
                    },
                    asset_upload_params.AssetUploadParams,
                ),
            ),
            cast_to=ReleaseAsset,
        )


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAssetsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        asset_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseAsset:
        """
        To download the asset's binary content:

        - If within a browser, fetch the location specified in the
          `browser_download_url` key provided in the response.
        - Alternatively, set the `Accept` header of the request to
          [`application/octet-stream`](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types).
          The API will either redirect the client to the location, or stream it directly
          if possible. API clients should handle both a `200` or `302` response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/releases/assets/{asset_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReleaseAsset,
        )

    async def update(
        self,
        asset_id: int,
        *,
        owner: str,
        repo: str,
        label: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        state: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseAsset:
        """
        Users with push access to the repository can edit a release asset.

        Args:
          label: An alternate short description of the asset. Used in place of the filename.

          name: The file name of the asset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._patch(
            f"/repos/{owner}/{repo}/releases/assets/{asset_id}",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "state": state,
                },
                asset_update_params.AssetUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReleaseAsset,
        )

    async def list(
        self,
        release_id: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AssetListResponse:
        """List release assets

        Args:
          page: The page number of the results to fetch.

        For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/releases/{release_id}/assets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            cast_to=AssetListResponse,
        )

    async def delete(
        self,
        asset_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete a release asset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/releases/assets/{asset_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def upload(
        self,
        release_id: int,
        *,
        owner: str,
        repo: str,
        name: str,
        label: str | NotGiven = NOT_GIVEN,
        body: FileTypes | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseAsset:
        """
        This endpoint makes use of a
        [Hypermedia relation](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia)
        to determine which URL to access. The endpoint you call to upload release assets
        is specific to your release. Use the `upload_url` returned in the response of
        the
        [Create a release endpoint](https://docs.github.com/rest/releases/releases#create-a-release)
        to upload a release asset.

        You need to use an HTTP client which supports
        [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) to make calls to this
        endpoint.

        Most libraries will set the required `Content-Length` header automatically. Use
        the required `Content-Type` header to provide the media type of the asset. For a
        list of media types, see
        [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml).
        For example:

        `application/zip`

        GitHub expects the asset data in its raw binary form, rather than JSON. You will
        send the raw binary content of the asset as the request body. Everything else
        about the endpoint is the same as the rest of the API. For example, you'll still
        need to pass your authentication to be able to upload an asset.

        When an upstream failure occurs, you will receive a `502 Bad Gateway` status.
        This may leave an empty asset with a state of `starter`. It can be safely
        deleted.

        **Notes:**

        - GitHub renames asset filenames that have special characters, non-alphanumeric
          characters, and leading or trailing periods. The
          "[List release assets](https://docs.github.com/rest/releases/assets#list-release-assets)"
          endpoint lists the renamed filenames. For more information and help, contact
          [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api).
        - To find the `release_id` query the
          [`GET /repos/{owner}/{repo}/releases/latest` endpoint](https://docs.github.com/rest/releases/releases#get-the-latest-release).
        - If you upload an asset with the same filename as another uploaded asset,
          you'll receive an error and must delete the old file before you can re-upload
          the new asset.

        Args:
          body: The raw file data

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
            f"/repos/{owner}/{repo}/releases/{release_id}/assets",
            body=await async_maybe_transform(body, asset_upload_params.AssetUploadParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "label": label,
                    },
                    asset_upload_params.AssetUploadParams,
                ),
            ),
            cast_to=ReleaseAsset,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.retrieve = to_raw_response_wrapper(
            assets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            assets.update,
        )
        self.list = to_raw_response_wrapper(
            assets.list,
        )
        self.delete = to_raw_response_wrapper(
            assets.delete,
        )
        self.upload = to_raw_response_wrapper(
            assets.upload,
        )


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.retrieve = async_to_raw_response_wrapper(
            assets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            assets.update,
        )
        self.list = async_to_raw_response_wrapper(
            assets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            assets.delete,
        )
        self.upload = async_to_raw_response_wrapper(
            assets.upload,
        )


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.retrieve = to_streamed_response_wrapper(
            assets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            assets.update,
        )
        self.list = to_streamed_response_wrapper(
            assets.list,
        )
        self.delete = to_streamed_response_wrapper(
            assets.delete,
        )
        self.upload = to_streamed_response_wrapper(
            assets.upload,
        )


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.retrieve = async_to_streamed_response_wrapper(
            assets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            assets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            assets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            assets.delete,
        )
        self.upload = async_to_streamed_response_wrapper(
            assets.upload,
        )
