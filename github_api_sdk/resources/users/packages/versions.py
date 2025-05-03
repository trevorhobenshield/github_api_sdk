from __future__ import annotations

import httpx
from typing_extensions import Literal

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.orgs.packages.package_version import PackageVersion
from ....types.users.packages import version_list_params
from ....types.users.packages.version_list_response import VersionListResponse
from ....types.users.packages.version_list_versions_response import VersionListVersionsResponse

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return VersionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        package_version_id: int,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageVersion:
        """
        Gets a specific package version for a package owned by the authenticated user.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return self._get(
            f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PackageVersion,
        )

    def list(
        self,
        package_name: str,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        state: Literal["active", "deleted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionListResponse:
        """
        Lists package versions for a package owned by the authenticated user.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          state: The state of the package, either active or deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return self._get(
            f"/user/packages/{package_type}/{package_name}/versions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "state": state,
                    },
                    version_list_params.VersionListParams,
                ),
            ),
            cast_to=VersionListResponse,
        )

    def delete(
        self,
        package_version_id: int,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a specific package version for a package owned by the authenticated
        user.

        If the package is public and the package version has more than 5,000
        downloads, you cannot delete the package version. In this scenario, contact
        GitHub support for further assistance.

        The authenticated user must have admin permissions in the organization to use
        this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        and `delete:packages` scopes to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def delete_version(
        self,
        package_version_id: int,
        *,
        username: str,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a specific package version for a user.

        If the package is public and the
        package version has more than 5,000 downloads, you cannot delete the package
        version. In this scenario, contact GitHub support for further assistance.

        If the `package_type` belongs to a GitHub Packages registry that supports
        granular permissions, the authenticated user must have admin permissions to the
        package. For the list of these registries, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)."

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        and `delete:packages` scopes to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list_versions(
        self,
        package_name: str,
        *,
        username: str,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionListVersionsResponse:
        """
        Lists package versions for a public package owned by a specified user.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return self._get(
            f"/users/{username}/packages/{package_type}/{package_name}/versions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=VersionListVersionsResponse,
        )

    def restore(
        self,
        package_version_id: int,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Restores a package version owned by the authenticated user.

        You can restore a deleted package version under the following conditions:

        - The package was deleted within the last 30 days.
        - The same package namespace and version is still available and not reused for a
          new package. If the same package namespace is not available, you will not be
          able to restore your package. In this scenario, to restore the deleted
          package, you must delete the new package that uses the deleted package's
          namespace first.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        and `write:packages` scopes to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}/restore",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def restore_version(
        self,
        package_version_id: int,
        *,
        username: str,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Restores a specific package version for a user.

        You can restore a deleted package under the following conditions:

        - The package was deleted within the last 30 days.
        - The same package namespace and version is still available and not reused for a
          new package. If the same package namespace is not available, you will not be
          able to restore your package. In this scenario, to restore the deleted
          package, you must delete the new package that uses the deleted package's
          namespace first.

        If the `package_type` belongs to a GitHub Packages registry that supports
        granular permissions, the authenticated user must have admin permissions to the
        package. For the list of these registries, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)."

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        and `write:packages` scopes to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}/restore",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def retrieve_version(
        self,
        package_version_id: int,
        *,
        username: str,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageVersion:
        """
        Gets a specific package version for a public package owned by a specified user.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return self._get(
            f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PackageVersion,
        )


class AsyncVersionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncVersionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        package_version_id: int,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageVersion:
        """
        Gets a specific package version for a package owned by the authenticated user.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return await self._get(
            f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PackageVersion,
        )

    async def list(
        self,
        package_name: str,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        state: Literal["active", "deleted"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionListResponse:
        """
        Lists package versions for a package owned by the authenticated user.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          state: The state of the package, either active or deleted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return await self._get(
            f"/user/packages/{package_type}/{package_name}/versions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "state": state,
                    },
                    version_list_params.VersionListParams,
                ),
            ),
            cast_to=VersionListResponse,
        )

    async def delete(
        self,
        package_version_id: int,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a specific package version for a package owned by the authenticated
        user.

        If the package is public and the package version has more than 5,000
        downloads, you cannot delete the package version. In this scenario, contact
        GitHub support for further assistance.

        The authenticated user must have admin permissions in the organization to use
        this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        and `delete:packages` scopes to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def delete_version(
        self,
        package_version_id: int,
        *,
        username: str,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a specific package version for a user.

        If the package is public and the
        package version has more than 5,000 downloads, you cannot delete the package
        version. In this scenario, contact GitHub support for further assistance.

        If the `package_type` belongs to a GitHub Packages registry that supports
        granular permissions, the authenticated user must have admin permissions to the
        package. For the list of these registries, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)."

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        and `delete:packages` scopes to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list_versions(
        self,
        package_name: str,
        *,
        username: str,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VersionListVersionsResponse:
        """
        Lists package versions for a public package owned by a specified user.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return await self._get(
            f"/users/{username}/packages/{package_type}/{package_name}/versions",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=VersionListVersionsResponse,
        )

    async def restore(
        self,
        package_version_id: int,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Restores a package version owned by the authenticated user.

        You can restore a deleted package version under the following conditions:

        - The package was deleted within the last 30 days.
        - The same package namespace and version is still available and not reused for a
          new package. If the same package namespace is not available, you will not be
          able to restore your package. In this scenario, to restore the deleted
          package, you must delete the new package that uses the deleted package's
          namespace first.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        and `write:packages` scopes to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/user/packages/{package_type}/{package_name}/versions/{package_version_id}/restore",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def restore_version(
        self,
        package_version_id: int,
        *,
        username: str,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Restores a specific package version for a user.

        You can restore a deleted package under the following conditions:

        - The package was deleted within the last 30 days.
        - The same package namespace and version is still available and not reused for a
          new package. If the same package namespace is not available, you will not be
          able to restore your package. In this scenario, to restore the deleted
          package, you must delete the new package that uses the deleted package's
          namespace first.

        If the `package_type` belongs to a GitHub Packages registry that supports
        granular permissions, the authenticated user must have admin permissions to the
        package. For the list of these registries, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)."

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        and `write:packages` scopes to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}/restore",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def retrieve_version(
        self,
        package_version_id: int,
        *,
        username: str,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        package_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageVersion:
        """
        Gets a specific package version for a public package owned by a specified user.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        if not package_type:
            raise ValueError(f"Expected a non-empty value for `package_type` but received {package_type!r}")
        if not package_name:
            raise ValueError(f"Expected a non-empty value for `package_name` but received {package_name!r}")
        return await self._get(
            f"/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PackageVersion,
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.retrieve = to_raw_response_wrapper(
            versions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            versions.list,
        )
        self.delete = to_raw_response_wrapper(
            versions.delete,
        )
        self.delete_version = to_raw_response_wrapper(
            versions.delete_version,
        )
        self.list_versions = to_raw_response_wrapper(
            versions.list_versions,
        )
        self.restore = to_raw_response_wrapper(
            versions.restore,
        )
        self.restore_version = to_raw_response_wrapper(
            versions.restore_version,
        )
        self.retrieve_version = to_raw_response_wrapper(
            versions.retrieve_version,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.retrieve = async_to_raw_response_wrapper(
            versions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            versions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            versions.delete,
        )
        self.delete_version = async_to_raw_response_wrapper(
            versions.delete_version,
        )
        self.list_versions = async_to_raw_response_wrapper(
            versions.list_versions,
        )
        self.restore = async_to_raw_response_wrapper(
            versions.restore,
        )
        self.restore_version = async_to_raw_response_wrapper(
            versions.restore_version,
        )
        self.retrieve_version = async_to_raw_response_wrapper(
            versions.retrieve_version,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.retrieve = to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            versions.list,
        )
        self.delete = to_streamed_response_wrapper(
            versions.delete,
        )
        self.delete_version = to_streamed_response_wrapper(
            versions.delete_version,
        )
        self.list_versions = to_streamed_response_wrapper(
            versions.list_versions,
        )
        self.restore = to_streamed_response_wrapper(
            versions.restore,
        )
        self.restore_version = to_streamed_response_wrapper(
            versions.restore_version,
        )
        self.retrieve_version = to_streamed_response_wrapper(
            versions.retrieve_version,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.retrieve = async_to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            versions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            versions.delete,
        )
        self.delete_version = async_to_streamed_response_wrapper(
            versions.delete_version,
        )
        self.list_versions = async_to_streamed_response_wrapper(
            versions.list_versions,
        )
        self.restore = async_to_streamed_response_wrapper(
            versions.restore,
        )
        self.restore_version = async_to_streamed_response_wrapper(
            versions.restore_version,
        )
        self.retrieve_version = async_to_streamed_response_wrapper(
            versions.retrieve_version,
        )
