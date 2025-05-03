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
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.repos.branches.protection import required_pull_request_review_update_params
from .....types.repos.branches.protection.protected_branch_pull_request_review import ProtectedBranchPullRequestReview

__all__ = ["RequiredPullRequestReviewsResource", "AsyncRequiredPullRequestReviewsResource"]


class RequiredPullRequestReviewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RequiredPullRequestReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return RequiredPullRequestReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RequiredPullRequestReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return RequiredPullRequestReviewsResourceWithStreamingResponse(self)

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
    ) -> ProtectedBranchPullRequestReview:
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
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectedBranchPullRequestReview,
        )

    def update(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        bypass_pull_request_allowances: required_pull_request_review_update_params.BypassPullRequestAllowances | NotGiven = NOT_GIVEN,
        dismiss_stale_reviews: bool | NotGiven = NOT_GIVEN,
        dismissal_restrictions: required_pull_request_review_update_params.DismissalRestrictions | NotGiven = NOT_GIVEN,
        require_code_owner_reviews: bool | NotGiven = NOT_GIVEN,
        require_last_push_approval: bool | NotGiven = NOT_GIVEN,
        required_approving_review_count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtectedBranchPullRequestReview:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Updating pull request review enforcement requires admin or owner permissions to
        the repository and branch protection to be enabled.

        > [!NOTE] Passing new arrays of `users` and `teams` replaces their previous
        > values.

        Args:
          bypass_pull_request_allowances: Allow specific users, teams, or apps to bypass pull request requirements.

          dismiss_stale_reviews: Set to `true` if you want to automatically dismiss approving reviews when
              someone pushes a new commit.

          dismissal_restrictions: Specify which users, teams, and apps can dismiss pull request reviews. Pass an
              empty `dismissal_restrictions` object to disable. User and team
              `dismissal_restrictions` are only available for organization-owned repositories.
              Omit this parameter for personal repositories.

          require_code_owner_reviews: Blocks merging pull requests until
              [code owners](https://docs.github.com/articles/about-code-owners/) have
              reviewed.

          require_last_push_approval: Whether the most recent push must be approved by someone other than the person
              who pushed it. Default: `false`

          required_approving_review_count: Specifies the number of reviewers required to approve pull requests. Use a
              number between 1 and 6 or 0 to not require reviewers.

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
        return self._patch(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
            body=maybe_transform(
                {
                    "bypass_pull_request_allowances": bypass_pull_request_allowances,
                    "dismiss_stale_reviews": dismiss_stale_reviews,
                    "dismissal_restrictions": dismissal_restrictions,
                    "require_code_owner_reviews": require_code_owner_reviews,
                    "require_last_push_approval": require_last_push_approval,
                    "required_approving_review_count": required_approving_review_count,
                },
                required_pull_request_review_update_params.RequiredPullRequestReviewUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectedBranchPullRequestReview,
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
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncRequiredPullRequestReviewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRequiredPullRequestReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRequiredPullRequestReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRequiredPullRequestReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncRequiredPullRequestReviewsResourceWithStreamingResponse(self)

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
    ) -> ProtectedBranchPullRequestReview:
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
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectedBranchPullRequestReview,
        )

    async def update(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        bypass_pull_request_allowances: required_pull_request_review_update_params.BypassPullRequestAllowances | NotGiven = NOT_GIVEN,
        dismiss_stale_reviews: bool | NotGiven = NOT_GIVEN,
        dismissal_restrictions: required_pull_request_review_update_params.DismissalRestrictions | NotGiven = NOT_GIVEN,
        require_code_owner_reviews: bool | NotGiven = NOT_GIVEN,
        require_last_push_approval: bool | NotGiven = NOT_GIVEN,
        required_approving_review_count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtectedBranchPullRequestReview:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Updating pull request review enforcement requires admin or owner permissions to
        the repository and branch protection to be enabled.

        > [!NOTE] Passing new arrays of `users` and `teams` replaces their previous
        > values.

        Args:
          bypass_pull_request_allowances: Allow specific users, teams, or apps to bypass pull request requirements.

          dismiss_stale_reviews: Set to `true` if you want to automatically dismiss approving reviews when
              someone pushes a new commit.

          dismissal_restrictions: Specify which users, teams, and apps can dismiss pull request reviews. Pass an
              empty `dismissal_restrictions` object to disable. User and team
              `dismissal_restrictions` are only available for organization-owned repositories.
              Omit this parameter for personal repositories.

          require_code_owner_reviews: Blocks merging pull requests until
              [code owners](https://docs.github.com/articles/about-code-owners/) have
              reviewed.

          require_last_push_approval: Whether the most recent push must be approved by someone other than the person
              who pushed it. Default: `false`

          required_approving_review_count: Specifies the number of reviewers required to approve pull requests. Use a
              number between 1 and 6 or 0 to not require reviewers.

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
        return await self._patch(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
            body=await async_maybe_transform(
                {
                    "bypass_pull_request_allowances": bypass_pull_request_allowances,
                    "dismiss_stale_reviews": dismiss_stale_reviews,
                    "dismissal_restrictions": dismissal_restrictions,
                    "require_code_owner_reviews": require_code_owner_reviews,
                    "require_last_push_approval": require_last_push_approval,
                    "required_approving_review_count": required_approving_review_count,
                },
                required_pull_request_review_update_params.RequiredPullRequestReviewUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectedBranchPullRequestReview,
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
            f"/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class RequiredPullRequestReviewsResourceWithRawResponse:
    def __init__(self, required_pull_request_reviews: RequiredPullRequestReviewsResource) -> None:
        self._required_pull_request_reviews = required_pull_request_reviews

        self.retrieve = to_raw_response_wrapper(
            required_pull_request_reviews.retrieve,
        )
        self.update = to_raw_response_wrapper(
            required_pull_request_reviews.update,
        )
        self.delete = to_raw_response_wrapper(
            required_pull_request_reviews.delete,
        )


class AsyncRequiredPullRequestReviewsResourceWithRawResponse:
    def __init__(self, required_pull_request_reviews: AsyncRequiredPullRequestReviewsResource) -> None:
        self._required_pull_request_reviews = required_pull_request_reviews

        self.retrieve = async_to_raw_response_wrapper(
            required_pull_request_reviews.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            required_pull_request_reviews.update,
        )
        self.delete = async_to_raw_response_wrapper(
            required_pull_request_reviews.delete,
        )


class RequiredPullRequestReviewsResourceWithStreamingResponse:
    def __init__(self, required_pull_request_reviews: RequiredPullRequestReviewsResource) -> None:
        self._required_pull_request_reviews = required_pull_request_reviews

        self.retrieve = to_streamed_response_wrapper(
            required_pull_request_reviews.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            required_pull_request_reviews.update,
        )
        self.delete = to_streamed_response_wrapper(
            required_pull_request_reviews.delete,
        )


class AsyncRequiredPullRequestReviewsResourceWithStreamingResponse:
    def __init__(self, required_pull_request_reviews: AsyncRequiredPullRequestReviewsResource) -> None:
        self._required_pull_request_reviews = required_pull_request_reviews

        self.retrieve = async_to_streamed_response_wrapper(
            required_pull_request_reviews.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            required_pull_request_reviews.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            required_pull_request_reviews.delete,
        )
