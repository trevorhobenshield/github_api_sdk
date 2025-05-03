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
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos import branch_list_params, branch_rename_params
from ....types.repos.branch_list_response import BranchListResponse
from ....types.repos.branch_with_protection import BranchWithProtection
from .protection.protection import (
    AsyncProtectionResource,
    AsyncProtectionResourceWithRawResponse,
    AsyncProtectionResourceWithStreamingResponse,
    ProtectionResource,
    ProtectionResourceWithRawResponse,
    ProtectionResourceWithStreamingResponse,
)

__all__ = ["BranchesResource", "AsyncBranchesResource"]


class BranchesResource(SyncAPIResource):
    @cached_property
    def protection(self) -> ProtectionResource:
        return ProtectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> BranchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return BranchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BranchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return BranchesResourceWithStreamingResponse(self)

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
    ) -> BranchWithProtection:
        """
        Get a branch

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
            f"/repos/{owner}/{repo}/branches/{branch}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BranchWithProtection,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        protected: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BranchListResponse:
        """List branches

        Args:
          page: The page number of the results to fetch.

        For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          protected: Setting to `true` returns only branches protected by branch protections or
              rulesets. When set to `false`, only unprotected branches are returned. Omitting
              this parameter returns all branches.

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
            f"/repos/{owner}/{repo}/branches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "protected": protected,
                    },
                    branch_list_params.BranchListParams,
                ),
            ),
            cast_to=BranchListResponse,
        )

    def rename(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        new_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BranchWithProtection:
        """
        Renames a branch in a repository.

        > [!NOTE] Although the API responds immediately, the branch rename process might
        > take some extra time to complete in the background. You won't be able to push
        > to the old branch name while the rename process is in progress. For more
        > information, see
        > "[Renaming a branch](https://docs.github.com/github/administering-a-repository/renaming-a-branch)".

        The authenticated user must have push access to the branch. If the branch is the
        default branch, the authenticated user must also have admin or owner
        permissions.

        In order to rename the default branch, fine-grained access tokens also need the
        `administration:write` repository permission.

        Args:
          new_name: The new name of the branch.

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
            f"/repos/{owner}/{repo}/branches/{branch}/rename",
            body=maybe_transform({"new_name": new_name}, branch_rename_params.BranchRenameParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BranchWithProtection,
        )


class AsyncBranchesResource(AsyncAPIResource):
    @cached_property
    def protection(self) -> AsyncProtectionResource:
        return AsyncProtectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBranchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBranchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBranchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncBranchesResourceWithStreamingResponse(self)

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
    ) -> BranchWithProtection:
        """
        Get a branch

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
            f"/repos/{owner}/{repo}/branches/{branch}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BranchWithProtection,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        protected: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BranchListResponse:
        """List branches

        Args:
          page: The page number of the results to fetch.

        For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          protected: Setting to `true` returns only branches protected by branch protections or
              rulesets. When set to `false`, only unprotected branches are returned. Omitting
              this parameter returns all branches.

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
            f"/repos/{owner}/{repo}/branches",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                        "protected": protected,
                    },
                    branch_list_params.BranchListParams,
                ),
            ),
            cast_to=BranchListResponse,
        )

    async def rename(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        new_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BranchWithProtection:
        """
        Renames a branch in a repository.

        > [!NOTE] Although the API responds immediately, the branch rename process might
        > take some extra time to complete in the background. You won't be able to push
        > to the old branch name while the rename process is in progress. For more
        > information, see
        > "[Renaming a branch](https://docs.github.com/github/administering-a-repository/renaming-a-branch)".

        The authenticated user must have push access to the branch. If the branch is the
        default branch, the authenticated user must also have admin or owner
        permissions.

        In order to rename the default branch, fine-grained access tokens also need the
        `administration:write` repository permission.

        Args:
          new_name: The new name of the branch.

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
            f"/repos/{owner}/{repo}/branches/{branch}/rename",
            body=await async_maybe_transform({"new_name": new_name}, branch_rename_params.BranchRenameParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BranchWithProtection,
        )


class BranchesResourceWithRawResponse:
    def __init__(self, branches: BranchesResource) -> None:
        self._branches = branches

        self.retrieve = to_raw_response_wrapper(
            branches.retrieve,
        )
        self.list = to_raw_response_wrapper(
            branches.list,
        )
        self.rename = to_raw_response_wrapper(
            branches.rename,
        )

    @cached_property
    def protection(self) -> ProtectionResourceWithRawResponse:
        return ProtectionResourceWithRawResponse(self._branches.protection)


class AsyncBranchesResourceWithRawResponse:
    def __init__(self, branches: AsyncBranchesResource) -> None:
        self._branches = branches

        self.retrieve = async_to_raw_response_wrapper(
            branches.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            branches.list,
        )
        self.rename = async_to_raw_response_wrapper(
            branches.rename,
        )

    @cached_property
    def protection(self) -> AsyncProtectionResourceWithRawResponse:
        return AsyncProtectionResourceWithRawResponse(self._branches.protection)


class BranchesResourceWithStreamingResponse:
    def __init__(self, branches: BranchesResource) -> None:
        self._branches = branches

        self.retrieve = to_streamed_response_wrapper(
            branches.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            branches.list,
        )
        self.rename = to_streamed_response_wrapper(
            branches.rename,
        )

    @cached_property
    def protection(self) -> ProtectionResourceWithStreamingResponse:
        return ProtectionResourceWithStreamingResponse(self._branches.protection)


class AsyncBranchesResourceWithStreamingResponse:
    def __init__(self, branches: AsyncBranchesResource) -> None:
        self._branches = branches

        self.retrieve = async_to_streamed_response_wrapper(
            branches.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            branches.list,
        )
        self.rename = async_to_streamed_response_wrapper(
            branches.rename,
        )

    @cached_property
    def protection(self) -> AsyncProtectionResourceWithStreamingResponse:
        return AsyncProtectionResourceWithStreamingResponse(self._branches.protection)
