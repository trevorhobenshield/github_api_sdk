from __future__ import annotations

import httpx

from ....._base_client import make_request_options
from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from ....._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ....._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from .....types.repos.branches.protection.protected_branch_admin_enforced import ProtectedBranchAdminEnforced

__all__ = ["EnforceAdminsResource", "AsyncEnforceAdminsResource"]


class EnforceAdminsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnforceAdminsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return EnforceAdminsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnforceAdminsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return EnforceAdminsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtectedBranchAdminEnforced:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return self._get(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectedBranchAdminEnforced,
        )

    def delete(
        self,
        branch: str,
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
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Removing admin enforcement requires admin or owner permissions to the repository
        and branch protection to be enabled.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def set(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtectedBranchAdminEnforced:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Adding admin enforcement requires admin or owner permissions to the repository
        and branch protection to be enabled.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return self._post(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectedBranchAdminEnforced,
        )


class AsyncEnforceAdminsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnforceAdminsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnforceAdminsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnforceAdminsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncEnforceAdminsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtectedBranchAdminEnforced:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectedBranchAdminEnforced,
        )

    async def delete(
        self,
        branch: str,
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
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Removing admin enforcement requires admin or owner permissions to the repository
        and branch protection to be enabled.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def set(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtectedBranchAdminEnforced:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Adding admin enforcement requires admin or owner permissions to the repository
        and branch protection to be enabled.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectedBranchAdminEnforced,
        )


class EnforceAdminsResourceWithRawResponse:
    def __init__(self, enforce_admins: EnforceAdminsResource) -> None:
        self._enforce_admins = enforce_admins

        self.retrieve = to_raw_response_wrapper(
            enforce_admins.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            enforce_admins.delete,
        )
        self.set = to_raw_response_wrapper(
            enforce_admins.set,
        )


class AsyncEnforceAdminsResourceWithRawResponse:
    def __init__(self, enforce_admins: AsyncEnforceAdminsResource) -> None:
        self._enforce_admins = enforce_admins

        self.retrieve = async_to_raw_response_wrapper(
            enforce_admins.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            enforce_admins.delete,
        )
        self.set = async_to_raw_response_wrapper(
            enforce_admins.set,
        )


class EnforceAdminsResourceWithStreamingResponse:
    def __init__(self, enforce_admins: EnforceAdminsResource) -> None:
        self._enforce_admins = enforce_admins

        self.retrieve = to_streamed_response_wrapper(
            enforce_admins.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            enforce_admins.delete,
        )
        self.set = to_streamed_response_wrapper(
            enforce_admins.set,
        )


class AsyncEnforceAdminsResourceWithStreamingResponse:
    def __init__(self, enforce_admins: AsyncEnforceAdminsResource) -> None:
        self._enforce_admins = enforce_admins

        self.retrieve = async_to_streamed_response_wrapper(
            enforce_admins.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            enforce_admins.delete,
        )
        self.set = async_to_streamed_response_wrapper(
            enforce_admins.set,
        )
