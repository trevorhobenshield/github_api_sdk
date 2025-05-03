from __future__ import annotations

from typing import Optional

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
from ....types.repos import page_create_params, page_update_params
from ....types.repos.page import Page
from ....types.repos.page_get_health_response import PageGetHealthResponse
from .builds import (
    AsyncBuildsResource,
    AsyncBuildsResourceWithRawResponse,
    AsyncBuildsResourceWithStreamingResponse,
    BuildsResource,
    BuildsResourceWithRawResponse,
    BuildsResourceWithStreamingResponse,
)
from .deployments import (
    AsyncDeploymentsResource,
    AsyncDeploymentsResourceWithRawResponse,
    AsyncDeploymentsResourceWithStreamingResponse,
    DeploymentsResource,
    DeploymentsResourceWithRawResponse,
    DeploymentsResourceWithStreamingResponse,
)

__all__ = ["PagesResource", "AsyncPagesResource"]


class PagesResource(SyncAPIResource):
    @cached_property
    def builds(self) -> BuildsResource:
        return BuildsResource(self._client)

    @cached_property
    def deployments(self) -> DeploymentsResource:
        return DeploymentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return PagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return PagesResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        build_type: Literal["legacy", "workflow"] | NotGiven = NOT_GIVEN,
        source: page_create_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Page:
        """Configures a GitHub Pages site.

        For more information, see
        "[About GitHub Pages](/github/working-with-github-pages/about-github-pages)."

        The authenticated user must be a repository administrator, maintainer, or have
        the 'manage GitHub Pages settings' permission.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          build_type: The process in which the Page will be built. Possible values are `"legacy"` and
              `"workflow"`.

          source: The source branch and directory used to publish your Pages site.

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
            f"/repos/{owner}/{repo}/pages",
            body=maybe_transform(
                {
                    "build_type": build_type,
                    "source": source,
                },
                page_create_params.PageCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Page,
        )

    def retrieve(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Page:
        """
        Gets information about a GitHub Pages site.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/pages",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Page,
        )

    def update(
        self,
        repo: str,
        *,
        owner: str,
        build_type: Literal["legacy", "workflow"] | NotGiven = NOT_GIVEN,
        cname: str | None | NotGiven = NOT_GIVEN,
        https_enforced: bool | NotGiven = NOT_GIVEN,
        source: page_update_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Updates information for a GitHub Pages site.

        For more information, see
        "[About GitHub Pages](/github/working-with-github-pages/about-github-pages).

        The authenticated user must be a repository administrator, maintainer, or have
        the 'manage GitHub Pages settings' permission.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          build_type: The process by which the GitHub Pages site will be built. `workflow` means that
              the site is built by a custom GitHub Actions workflow. `legacy` means that the
              site is built by GitHub when changes are pushed to a specific branch.

          cname: Specify a custom domain for the repository. Sending a `null` value will remove
              the custom domain. For more about custom domains, see
              "[Using a custom domain with GitHub Pages](https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site)."

          https_enforced: Specify whether HTTPS should be enforced for the repository.

          source: Update the source for the repository. Must include the branch name, and may
              optionally specify the subdirectory `/docs`. Possible values are `"gh-pages"`,
              `"master"`, and `"master /docs"`.

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
        return self._put(
            f"/repos/{owner}/{repo}/pages",
            body=maybe_transform(
                {
                    "build_type": build_type,
                    "cname": cname,
                    "https_enforced": https_enforced,
                    "source": source,
                },
                page_update_params.PageUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def delete(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a GitHub Pages site.

        For more information, see
        "[About GitHub Pages](/github/working-with-github-pages/about-github-pages).

        The authenticated user must be a repository administrator, maintainer, or have
        the 'manage GitHub Pages settings' permission.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/pages",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def get_health(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageGetHealthResponse:
        """
        Gets a health check of the DNS settings for the `CNAME` record configured for a
        repository's GitHub Pages.

        The first request to this endpoint returns a `202 Accepted` status and starts an
        asynchronous background task to get the results for the domain. After the
        background task completes, subsequent requests to this endpoint return a
        `200 OK` status with the health check results in the response.

        The authenticated user must be a repository administrator, maintainer, or have
        the 'manage GitHub Pages settings' permission to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/pages/health",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PageGetHealthResponse,
        )


class AsyncPagesResource(AsyncAPIResource):
    @cached_property
    def builds(self) -> AsyncBuildsResource:
        return AsyncBuildsResource(self._client)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        return AsyncDeploymentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncPagesResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        build_type: Literal["legacy", "workflow"] | NotGiven = NOT_GIVEN,
        source: page_create_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Page:
        """Configures a GitHub Pages site.

        For more information, see
        "[About GitHub Pages](/github/working-with-github-pages/about-github-pages)."

        The authenticated user must be a repository administrator, maintainer, or have
        the 'manage GitHub Pages settings' permission.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          build_type: The process in which the Page will be built. Possible values are `"legacy"` and
              `"workflow"`.

          source: The source branch and directory used to publish your Pages site.

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
            f"/repos/{owner}/{repo}/pages",
            body=await async_maybe_transform(
                {
                    "build_type": build_type,
                    "source": source,
                },
                page_create_params.PageCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Page,
        )

    async def retrieve(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Page:
        """
        Gets information about a GitHub Pages site.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/pages",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Page,
        )

    async def update(
        self,
        repo: str,
        *,
        owner: str,
        build_type: Literal["legacy", "workflow"] | NotGiven = NOT_GIVEN,
        cname: str | None | NotGiven = NOT_GIVEN,
        https_enforced: bool | NotGiven = NOT_GIVEN,
        source: page_update_params.Source | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Updates information for a GitHub Pages site.

        For more information, see
        "[About GitHub Pages](/github/working-with-github-pages/about-github-pages).

        The authenticated user must be a repository administrator, maintainer, or have
        the 'manage GitHub Pages settings' permission.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          build_type: The process by which the GitHub Pages site will be built. `workflow` means that
              the site is built by a custom GitHub Actions workflow. `legacy` means that the
              site is built by GitHub when changes are pushed to a specific branch.

          cname: Specify a custom domain for the repository. Sending a `null` value will remove
              the custom domain. For more about custom domains, see
              "[Using a custom domain with GitHub Pages](https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site)."

          https_enforced: Specify whether HTTPS should be enforced for the repository.

          source: Update the source for the repository. Must include the branch name, and may
              optionally specify the subdirectory `/docs`. Possible values are `"gh-pages"`,
              `"master"`, and `"master /docs"`.

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
        return await self._put(
            f"/repos/{owner}/{repo}/pages",
            body=await async_maybe_transform(
                {
                    "build_type": build_type,
                    "cname": cname,
                    "https_enforced": https_enforced,
                    "source": source,
                },
                page_update_params.PageUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def delete(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes a GitHub Pages site.

        For more information, see
        "[About GitHub Pages](/github/working-with-github-pages/about-github-pages).

        The authenticated user must be a repository administrator, maintainer, or have
        the 'manage GitHub Pages settings' permission.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/pages",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def get_health(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PageGetHealthResponse:
        """
        Gets a health check of the DNS settings for the `CNAME` record configured for a
        repository's GitHub Pages.

        The first request to this endpoint returns a `202 Accepted` status and starts an
        asynchronous background task to get the results for the domain. After the
        background task completes, subsequent requests to this endpoint return a
        `200 OK` status with the health check results in the response.

        The authenticated user must be a repository administrator, maintainer, or have
        the 'manage GitHub Pages settings' permission to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

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
            f"/repos/{owner}/{repo}/pages/health",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PageGetHealthResponse,
        )


class PagesResourceWithRawResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.create = to_raw_response_wrapper(
            pages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pages.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pages.update,
        )
        self.delete = to_raw_response_wrapper(
            pages.delete,
        )
        self.get_health = to_raw_response_wrapper(
            pages.get_health,
        )

    @cached_property
    def builds(self) -> BuildsResourceWithRawResponse:
        return BuildsResourceWithRawResponse(self._pages.builds)

    @cached_property
    def deployments(self) -> DeploymentsResourceWithRawResponse:
        return DeploymentsResourceWithRawResponse(self._pages.deployments)


class AsyncPagesResourceWithRawResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.create = async_to_raw_response_wrapper(
            pages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pages.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pages.update,
        )
        self.delete = async_to_raw_response_wrapper(
            pages.delete,
        )
        self.get_health = async_to_raw_response_wrapper(
            pages.get_health,
        )

    @cached_property
    def builds(self) -> AsyncBuildsResourceWithRawResponse:
        return AsyncBuildsResourceWithRawResponse(self._pages.builds)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithRawResponse:
        return AsyncDeploymentsResourceWithRawResponse(self._pages.deployments)


class PagesResourceWithStreamingResponse:
    def __init__(self, pages: PagesResource) -> None:
        self._pages = pages

        self.create = to_streamed_response_wrapper(
            pages.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pages.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pages.update,
        )
        self.delete = to_streamed_response_wrapper(
            pages.delete,
        )
        self.get_health = to_streamed_response_wrapper(
            pages.get_health,
        )

    @cached_property
    def builds(self) -> BuildsResourceWithStreamingResponse:
        return BuildsResourceWithStreamingResponse(self._pages.builds)

    @cached_property
    def deployments(self) -> DeploymentsResourceWithStreamingResponse:
        return DeploymentsResourceWithStreamingResponse(self._pages.deployments)


class AsyncPagesResourceWithStreamingResponse:
    def __init__(self, pages: AsyncPagesResource) -> None:
        self._pages = pages

        self.create = async_to_streamed_response_wrapper(
            pages.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pages.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pages.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            pages.delete,
        )
        self.get_health = async_to_streamed_response_wrapper(
            pages.get_health,
        )

    @cached_property
    def builds(self) -> AsyncBuildsResourceWithStreamingResponse:
        return AsyncBuildsResourceWithStreamingResponse(self._pages.builds)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResourceWithStreamingResponse:
        return AsyncDeploymentsResourceWithStreamingResponse(self._pages.deployments)
