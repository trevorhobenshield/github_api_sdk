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
from ....types.orgs.package import Package
from ....types.users import (
    package_list_packages_params,
    package_list_params,
    package_restore_package_params,
    package_restore_params,
)
from ....types.users.package_list_packages_response import PackageListPackagesResponse
from ....types.users.package_list_response import PackageListResponse
from .versions import (
    AsyncVersionsResource,
    AsyncVersionsResourceWithRawResponse,
    AsyncVersionsResourceWithStreamingResponse,
    VersionsResource,
    VersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
)

__all__ = ["PackagesResource", "AsyncPackagesResource"]


class PackagesResource(SyncAPIResource):
    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PackagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return PackagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PackagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return PackagesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        package_name: str,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Package:
        """
        Gets a specific package for a package owned by the authenticated user.

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
            f"/user/packages/{package_type}/{package_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Package,
        )

    def list(
        self,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private", "internal"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageListResponse:
        """
        Lists packages owned by the authenticated user within the user's namespace.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          package_type: The type of supported package. Packages in GitHub's Gradle registry have the
              type `maven`. Docker images pushed to GitHub's Container registry (`ghcr.io`)
              have the type `container`. You can use the type `docker` to find images that
              were pushed to GitHub's Docker registry (`docker.pkg.github.com`), even if these
              have now been migrated to the Container registry.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          visibility: The selected visibility of the packages. This parameter is optional and only
              filters an existing result set.

              The `internal` visibility is only supported for GitHub Packages registries that
              allow for granular permissions. For other ecosystems `internal` is synonymous
              with `private`. For the list of GitHub Packages registries that support granular
              permissions, see
              "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/packages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "package_type": package_type,
                        "page": page,
                        "per_page": per_page,
                        "visibility": visibility,
                    },
                    package_list_params.PackageListParams,
                ),
            ),
            cast_to=PackageListResponse,
        )

    def delete(
        self,
        package_name: str,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a package owned by the authenticated user.

        You cannot delete a public
        package if any version of the package has more than 5,000 downloads. In this
        scenario, contact GitHub support for further assistance.

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
            f"/user/packages/{package_type}/{package_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def delete_package(
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
    ) -> None:
        """Deletes an entire package for a user.

        You cannot delete a public package if any
        version of the package has more than 5,000 downloads. In this scenario, contact
        GitHub support for further assistance.

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
            f"/users/{username}/packages/{package_type}/{package_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list_packages(
        self,
        username: str,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private", "internal"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageListPackagesResponse:
        """
        Lists all packages in a user's namespace for which the requesting user has
        access.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          package_type: The type of supported package. Packages in GitHub's Gradle registry have the
              type `maven`. Docker images pushed to GitHub's Container registry (`ghcr.io`)
              have the type `container`. You can use the type `docker` to find images that
              were pushed to GitHub's Docker registry (`docker.pkg.github.com`), even if these
              have now been migrated to the Container registry.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          visibility: The selected visibility of the packages. This parameter is optional and only
              filters an existing result set.

              The `internal` visibility is only supported for GitHub Packages registries that
              allow for granular permissions. For other ecosystems `internal` is synonymous
              with `private`. For the list of GitHub Packages registries that support granular
              permissions, see
              "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/users/{username}/packages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "package_type": package_type,
                        "page": page,
                        "per_page": per_page,
                        "visibility": visibility,
                    },
                    package_list_packages_params.PackageListPackagesParams,
                ),
            ),
            cast_to=PackageListPackagesResponse,
        )

    def restore(
        self,
        package_name: str,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Restores a package owned by the authenticated user.

        You can restore a deleted package under the following conditions:

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
          token: package token

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
            f"/user/packages/{package_type}/{package_name}/restore",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"token": token}, package_restore_params.PackageRestoreParams),
            ),
            cast_to=NoneType,
        )

    def restore_package(
        self,
        package_name: str,
        *,
        username: str,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Restores an entire package for a user.

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
          token: package token

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
            f"/users/{username}/packages/{package_type}/{package_name}/restore",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"token": token}, package_restore_package_params.PackageRestorePackageParams),
            ),
            cast_to=NoneType,
        )

    def retrieve_package(
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
    ) -> Package:
        """
        Gets a specific package metadata for a public package owned by a user.

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
            f"/users/{username}/packages/{package_type}/{package_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Package,
        )


class AsyncPackagesResource(AsyncAPIResource):
    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPackagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPackagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPackagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncPackagesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        package_name: str,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Package:
        """
        Gets a specific package for a package owned by the authenticated user.

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
            f"/user/packages/{package_type}/{package_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Package,
        )

    async def list(
        self,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private", "internal"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageListResponse:
        """
        Lists packages owned by the authenticated user within the user's namespace.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          package_type: The type of supported package. Packages in GitHub's Gradle registry have the
              type `maven`. Docker images pushed to GitHub's Container registry (`ghcr.io`)
              have the type `container`. You can use the type `docker` to find images that
              were pushed to GitHub's Docker registry (`docker.pkg.github.com`), even if these
              have now been migrated to the Container registry.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          visibility: The selected visibility of the packages. This parameter is optional and only
              filters an existing result set.

              The `internal` visibility is only supported for GitHub Packages registries that
              allow for granular permissions. For other ecosystems `internal` is synonymous
              with `private`. For the list of GitHub Packages registries that support granular
              permissions, see
              "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/packages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "package_type": package_type,
                        "page": page,
                        "per_page": per_page,
                        "visibility": visibility,
                    },
                    package_list_params.PackageListParams,
                ),
            ),
            cast_to=PackageListResponse,
        )

    async def delete(
        self,
        package_name: str,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a package owned by the authenticated user.

        You cannot delete a public
        package if any version of the package has more than 5,000 downloads. In this
        scenario, contact GitHub support for further assistance.

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
            f"/user/packages/{package_type}/{package_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def delete_package(
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
    ) -> None:
        """Deletes an entire package for a user.

        You cannot delete a public package if any
        version of the package has more than 5,000 downloads. In this scenario, contact
        GitHub support for further assistance.

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
            f"/users/{username}/packages/{package_type}/{package_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list_packages(
        self,
        username: str,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private", "internal"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PackageListPackagesResponse:
        """
        Lists all packages in a user's namespace for which the requesting user has
        access.

        OAuth app tokens and personal access tokens (classic) need the `read:packages`
        scope to use this endpoint. For more information, see
        "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."

        Args:
          package_type: The type of supported package. Packages in GitHub's Gradle registry have the
              type `maven`. Docker images pushed to GitHub's Container registry (`ghcr.io`)
              have the type `container`. You can use the type `docker` to find images that
              were pushed to GitHub's Docker registry (`docker.pkg.github.com`), even if these
              have now been migrated to the Container registry.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          visibility: The selected visibility of the packages. This parameter is optional and only
              filters an existing result set.

              The `internal` visibility is only supported for GitHub Packages registries that
              allow for granular permissions. For other ecosystems `internal` is synonymous
              with `private`. For the list of GitHub Packages registries that support granular
              permissions, see
              "[About permissions for GitHub Packages](https://docs.github.com/packages/learn-github-packages/about-permissions-for-github-packages#granular-permissions-for-userorganization-scoped-packages)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/users/{username}/packages",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "package_type": package_type,
                        "page": page,
                        "per_page": per_page,
                        "visibility": visibility,
                    },
                    package_list_packages_params.PackageListPackagesParams,
                ),
            ),
            cast_to=PackageListPackagesResponse,
        )

    async def restore(
        self,
        package_name: str,
        *,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Restores a package owned by the authenticated user.

        You can restore a deleted package under the following conditions:

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
          token: package token

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
            f"/user/packages/{package_type}/{package_name}/restore",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"token": token}, package_restore_params.PackageRestoreParams),
            ),
            cast_to=NoneType,
        )

    async def restore_package(
        self,
        package_name: str,
        *,
        username: str,
        package_type: Literal["npm", "maven", "rubygems", "docker", "nuget", "container"],
        token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Restores an entire package for a user.

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
          token: package token

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
            f"/users/{username}/packages/{package_type}/{package_name}/restore",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"token": token}, package_restore_package_params.PackageRestorePackageParams),
            ),
            cast_to=NoneType,
        )

    async def retrieve_package(
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
    ) -> Package:
        """
        Gets a specific package metadata for a public package owned by a user.

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
            f"/users/{username}/packages/{package_type}/{package_name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Package,
        )


class PackagesResourceWithRawResponse:
    def __init__(self, packages: PackagesResource) -> None:
        self._packages = packages

        self.retrieve = to_raw_response_wrapper(
            packages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            packages.list,
        )
        self.delete = to_raw_response_wrapper(
            packages.delete,
        )
        self.delete_package = to_raw_response_wrapper(
            packages.delete_package,
        )
        self.list_packages = to_raw_response_wrapper(
            packages.list_packages,
        )
        self.restore = to_raw_response_wrapper(
            packages.restore,
        )
        self.restore_package = to_raw_response_wrapper(
            packages.restore_package,
        )
        self.retrieve_package = to_raw_response_wrapper(
            packages.retrieve_package,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._packages.versions)


class AsyncPackagesResourceWithRawResponse:
    def __init__(self, packages: AsyncPackagesResource) -> None:
        self._packages = packages

        self.retrieve = async_to_raw_response_wrapper(
            packages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            packages.list,
        )
        self.delete = async_to_raw_response_wrapper(
            packages.delete,
        )
        self.delete_package = async_to_raw_response_wrapper(
            packages.delete_package,
        )
        self.list_packages = async_to_raw_response_wrapper(
            packages.list_packages,
        )
        self.restore = async_to_raw_response_wrapper(
            packages.restore,
        )
        self.restore_package = async_to_raw_response_wrapper(
            packages.restore_package,
        )
        self.retrieve_package = async_to_raw_response_wrapper(
            packages.retrieve_package,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._packages.versions)


class PackagesResourceWithStreamingResponse:
    def __init__(self, packages: PackagesResource) -> None:
        self._packages = packages

        self.retrieve = to_streamed_response_wrapper(
            packages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            packages.list,
        )
        self.delete = to_streamed_response_wrapper(
            packages.delete,
        )
        self.delete_package = to_streamed_response_wrapper(
            packages.delete_package,
        )
        self.list_packages = to_streamed_response_wrapper(
            packages.list_packages,
        )
        self.restore = to_streamed_response_wrapper(
            packages.restore,
        )
        self.restore_package = to_streamed_response_wrapper(
            packages.restore_package,
        )
        self.retrieve_package = to_streamed_response_wrapper(
            packages.retrieve_package,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._packages.versions)


class AsyncPackagesResourceWithStreamingResponse:
    def __init__(self, packages: AsyncPackagesResource) -> None:
        self._packages = packages

        self.retrieve = async_to_streamed_response_wrapper(
            packages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            packages.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            packages.delete,
        )
        self.delete_package = async_to_streamed_response_wrapper(
            packages.delete_package,
        )
        self.list_packages = async_to_streamed_response_wrapper(
            packages.list_packages,
        )
        self.restore = async_to_streamed_response_wrapper(
            packages.restore,
        )
        self.restore_package = async_to_streamed_response_wrapper(
            packages.restore_package,
        )
        self.retrieve_package = async_to_streamed_response_wrapper(
            packages.retrieve_package,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._packages.versions)
