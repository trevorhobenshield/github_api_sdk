from __future__ import annotations

from typing import Optional

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
from .....types.repos.branches import protection_update_params
from .....types.repos.branches.branch_protection import BranchProtection
from .....types.repos.branches.protection_update_response import ProtectionUpdateResponse
from .enforce_admins import (
    AsyncEnforceAdminsResource,
    AsyncEnforceAdminsResourceWithRawResponse,
    AsyncEnforceAdminsResourceWithStreamingResponse,
    EnforceAdminsResource,
    EnforceAdminsResourceWithRawResponse,
    EnforceAdminsResourceWithStreamingResponse,
)
from .required_pull_request_reviews import (
    AsyncRequiredPullRequestReviewsResource,
    AsyncRequiredPullRequestReviewsResourceWithRawResponse,
    AsyncRequiredPullRequestReviewsResourceWithStreamingResponse,
    RequiredPullRequestReviewsResource,
    RequiredPullRequestReviewsResourceWithRawResponse,
    RequiredPullRequestReviewsResourceWithStreamingResponse,
)
from .required_signatures import (
    AsyncRequiredSignaturesResource,
    AsyncRequiredSignaturesResourceWithRawResponse,
    AsyncRequiredSignaturesResourceWithStreamingResponse,
    RequiredSignaturesResource,
    RequiredSignaturesResourceWithRawResponse,
    RequiredSignaturesResourceWithStreamingResponse,
)
from .required_status_checks.required_status_checks import (
    AsyncRequiredStatusChecksResource,
    AsyncRequiredStatusChecksResourceWithRawResponse,
    AsyncRequiredStatusChecksResourceWithStreamingResponse,
    RequiredStatusChecksResource,
    RequiredStatusChecksResourceWithRawResponse,
    RequiredStatusChecksResourceWithStreamingResponse,
)
from .restrictions.restrictions import (
    AsyncRestrictionsResource,
    AsyncRestrictionsResourceWithRawResponse,
    AsyncRestrictionsResourceWithStreamingResponse,
    RestrictionsResource,
    RestrictionsResourceWithRawResponse,
    RestrictionsResourceWithStreamingResponse,
)

__all__ = ["ProtectionResource", "AsyncProtectionResource"]


class ProtectionResource(SyncAPIResource):
    @cached_property
    def enforce_admins(self) -> EnforceAdminsResource:
        return EnforceAdminsResource(self._client)

    @cached_property
    def required_pull_request_reviews(self) -> RequiredPullRequestReviewsResource:
        return RequiredPullRequestReviewsResource(self._client)

    @cached_property
    def required_signatures(self) -> RequiredSignaturesResource:
        return RequiredSignaturesResource(self._client)

    @cached_property
    def required_status_checks(self) -> RequiredStatusChecksResource:
        return RequiredStatusChecksResource(self._client)

    @cached_property
    def restrictions(self) -> RestrictionsResource:
        return RestrictionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ProtectionResourceWithStreamingResponse(self)

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
    ) -> BranchProtection:
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
            f"/repos/{owner}/{repo}/branches/{branch}/protection",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BranchProtection,
        )

    def update(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        enforce_admins: bool | None,
        required_pull_request_reviews: protection_update_params.RequiredPullRequestReviews | None,
        required_status_checks: protection_update_params.RequiredStatusChecks | None,
        restrictions: protection_update_params.Restrictions | None,
        allow_deletions: bool | NotGiven = NOT_GIVEN,
        allow_force_pushes: bool | None | NotGiven = NOT_GIVEN,
        allow_fork_syncing: bool | NotGiven = NOT_GIVEN,
        block_creations: bool | NotGiven = NOT_GIVEN,
        lock_branch: bool | NotGiven = NOT_GIVEN,
        required_conversation_resolution: bool | NotGiven = NOT_GIVEN,
        required_linear_history: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtectionUpdateResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Protecting a branch requires admin or owner permissions to the repository.

        > [!NOTE] Passing new arrays of `users` and `teams` replaces their previous
        > values.

        > [!NOTE] The list of users, apps, and teams in total is limited to 100 items.

        Args:
          enforce_admins: Enforce all configured restrictions for administrators. Set to `true` to enforce
              required status checks for repository administrators. Set to `null` to disable.

          required_pull_request_reviews: Require at least one approving review on a pull request, before merging. Set to
              `null` to disable.

          required_status_checks: Require status checks to pass before merging. Set to `null` to disable.

          restrictions: Restrict who can push to the protected branch. User, app, and team
              `restrictions` are only available for organization-owned repositories. Set to
              `null` to disable.

          allow_deletions: Allows deletion of the protected branch by anyone with write access to the
              repository. Set to `false` to prevent deletion of the protected branch. Default:
              `false`. For more information, see
              "[Enabling force pushes to a protected branch](https://docs.github.com/github/administering-a-repository/enabling-force-pushes-to-a-protected-branch)"
              in the GitHub Help documentation.

          allow_force_pushes: Permits force pushes to the protected branch by anyone with write access to the
              repository. Set to `true` to allow force pushes. Set to `false` or `null` to
              block force pushes. Default: `false`. For more information, see
              "[Enabling force pushes to a protected branch](https://docs.github.com/github/administering-a-repository/enabling-force-pushes-to-a-protected-branch)"
              in the GitHub Help documentation."

          allow_fork_syncing: Whether users can pull changes from upstream when the branch is locked. Set to
              `true` to allow fork syncing. Set to `false` to prevent fork syncing. Default:
              `false`.

          block_creations: If set to `true`, the `restrictions` branch protection settings which limits who
              can push will also block pushes which create new branches, unless the push is
              initiated by a user, team, or app which has the ability to push. Set to `true`
              to restrict new branch creation. Default: `false`.

          lock_branch: Whether to set the branch as read-only. If this is true, users will not be able
              to push to the branch. Default: `false`.

          required_conversation_resolution: Requires all conversations on code to be resolved before a pull request can be
              merged into a branch that matches this rule. Set to `false` to disable. Default:
              `false`.

          required_linear_history: Enforces a linear commit Git history, which prevents anyone from pushing merge
              commits to a branch. Set to `true` to enforce a linear commit history. Set to
              `false` to disable a linear commit Git history. Your repository must allow
              squash merging or rebase merging before you can enable a linear commit history.
              Default: `false`. For more information, see
              "[Requiring a linear commit history](https://docs.github.com/github/administering-a-repository/requiring-a-linear-commit-history)"
              in the GitHub Help documentation.

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
        return self._put(
            f"/repos/{owner}/{repo}/branches/{branch}/protection",
            body=maybe_transform(
                {
                    "enforce_admins": enforce_admins,
                    "required_pull_request_reviews": required_pull_request_reviews,
                    "required_status_checks": required_status_checks,
                    "restrictions": restrictions,
                    "allow_deletions": allow_deletions,
                    "allow_force_pushes": allow_force_pushes,
                    "allow_fork_syncing": allow_fork_syncing,
                    "block_creations": block_creations,
                    "lock_branch": lock_branch,
                    "required_conversation_resolution": required_conversation_resolution,
                    "required_linear_history": required_linear_history,
                },
                protection_update_params.ProtectionUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectionUpdateResponse,
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
            f"/repos/{owner}/{repo}/branches/{branch}/protection",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncProtectionResource(AsyncAPIResource):
    @cached_property
    def enforce_admins(self) -> AsyncEnforceAdminsResource:
        return AsyncEnforceAdminsResource(self._client)

    @cached_property
    def required_pull_request_reviews(self) -> AsyncRequiredPullRequestReviewsResource:
        return AsyncRequiredPullRequestReviewsResource(self._client)

    @cached_property
    def required_signatures(self) -> AsyncRequiredSignaturesResource:
        return AsyncRequiredSignaturesResource(self._client)

    @cached_property
    def required_status_checks(self) -> AsyncRequiredStatusChecksResource:
        return AsyncRequiredStatusChecksResource(self._client)

    @cached_property
    def restrictions(self) -> AsyncRestrictionsResource:
        return AsyncRestrictionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProtectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProtectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProtectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncProtectionResourceWithStreamingResponse(self)

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
    ) -> BranchProtection:
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
            f"/repos/{owner}/{repo}/branches/{branch}/protection",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=BranchProtection,
        )

    async def update(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        enforce_admins: bool | None,
        required_pull_request_reviews: protection_update_params.RequiredPullRequestReviews | None,
        required_status_checks: protection_update_params.RequiredStatusChecks | None,
        restrictions: protection_update_params.Restrictions | None,
        allow_deletions: bool | NotGiven = NOT_GIVEN,
        allow_force_pushes: bool | None | NotGiven = NOT_GIVEN,
        allow_fork_syncing: bool | NotGiven = NOT_GIVEN,
        block_creations: bool | NotGiven = NOT_GIVEN,
        lock_branch: bool | NotGiven = NOT_GIVEN,
        required_conversation_resolution: bool | NotGiven = NOT_GIVEN,
        required_linear_history: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProtectionUpdateResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Protecting a branch requires admin or owner permissions to the repository.

        > [!NOTE] Passing new arrays of `users` and `teams` replaces their previous
        > values.

        > [!NOTE] The list of users, apps, and teams in total is limited to 100 items.

        Args:
          enforce_admins: Enforce all configured restrictions for administrators. Set to `true` to enforce
              required status checks for repository administrators. Set to `null` to disable.

          required_pull_request_reviews: Require at least one approving review on a pull request, before merging. Set to
              `null` to disable.

          required_status_checks: Require status checks to pass before merging. Set to `null` to disable.

          restrictions: Restrict who can push to the protected branch. User, app, and team
              `restrictions` are only available for organization-owned repositories. Set to
              `null` to disable.

          allow_deletions: Allows deletion of the protected branch by anyone with write access to the
              repository. Set to `false` to prevent deletion of the protected branch. Default:
              `false`. For more information, see
              "[Enabling force pushes to a protected branch](https://docs.github.com/github/administering-a-repository/enabling-force-pushes-to-a-protected-branch)"
              in the GitHub Help documentation.

          allow_force_pushes: Permits force pushes to the protected branch by anyone with write access to the
              repository. Set to `true` to allow force pushes. Set to `false` or `null` to
              block force pushes. Default: `false`. For more information, see
              "[Enabling force pushes to a protected branch](https://docs.github.com/github/administering-a-repository/enabling-force-pushes-to-a-protected-branch)"
              in the GitHub Help documentation."

          allow_fork_syncing: Whether users can pull changes from upstream when the branch is locked. Set to
              `true` to allow fork syncing. Set to `false` to prevent fork syncing. Default:
              `false`.

          block_creations: If set to `true`, the `restrictions` branch protection settings which limits who
              can push will also block pushes which create new branches, unless the push is
              initiated by a user, team, or app which has the ability to push. Set to `true`
              to restrict new branch creation. Default: `false`.

          lock_branch: Whether to set the branch as read-only. If this is true, users will not be able
              to push to the branch. Default: `false`.

          required_conversation_resolution: Requires all conversations on code to be resolved before a pull request can be
              merged into a branch that matches this rule. Set to `false` to disable. Default:
              `false`.

          required_linear_history: Enforces a linear commit Git history, which prevents anyone from pushing merge
              commits to a branch. Set to `true` to enforce a linear commit history. Set to
              `false` to disable a linear commit Git history. Your repository must allow
              squash merging or rebase merging before you can enable a linear commit history.
              Default: `false`. For more information, see
              "[Requiring a linear commit history](https://docs.github.com/github/administering-a-repository/requiring-a-linear-commit-history)"
              in the GitHub Help documentation.

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
        return await self._put(
            f"/repos/{owner}/{repo}/branches/{branch}/protection",
            body=await async_maybe_transform(
                {
                    "enforce_admins": enforce_admins,
                    "required_pull_request_reviews": required_pull_request_reviews,
                    "required_status_checks": required_status_checks,
                    "restrictions": restrictions,
                    "allow_deletions": allow_deletions,
                    "allow_force_pushes": allow_force_pushes,
                    "allow_fork_syncing": allow_fork_syncing,
                    "block_creations": block_creations,
                    "lock_branch": lock_branch,
                    "required_conversation_resolution": required_conversation_resolution,
                    "required_linear_history": required_linear_history,
                },
                protection_update_params.ProtectionUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ProtectionUpdateResponse,
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
            f"/repos/{owner}/{repo}/branches/{branch}/protection",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class ProtectionResourceWithRawResponse:
    def __init__(self, protection: ProtectionResource) -> None:
        self._protection = protection

        self.retrieve = to_raw_response_wrapper(
            protection.retrieve,
        )
        self.update = to_raw_response_wrapper(
            protection.update,
        )
        self.delete = to_raw_response_wrapper(
            protection.delete,
        )

    @cached_property
    def enforce_admins(self) -> EnforceAdminsResourceWithRawResponse:
        return EnforceAdminsResourceWithRawResponse(self._protection.enforce_admins)

    @cached_property
    def required_pull_request_reviews(self) -> RequiredPullRequestReviewsResourceWithRawResponse:
        return RequiredPullRequestReviewsResourceWithRawResponse(self._protection.required_pull_request_reviews)

    @cached_property
    def required_signatures(self) -> RequiredSignaturesResourceWithRawResponse:
        return RequiredSignaturesResourceWithRawResponse(self._protection.required_signatures)

    @cached_property
    def required_status_checks(self) -> RequiredStatusChecksResourceWithRawResponse:
        return RequiredStatusChecksResourceWithRawResponse(self._protection.required_status_checks)

    @cached_property
    def restrictions(self) -> RestrictionsResourceWithRawResponse:
        return RestrictionsResourceWithRawResponse(self._protection.restrictions)


class AsyncProtectionResourceWithRawResponse:
    def __init__(self, protection: AsyncProtectionResource) -> None:
        self._protection = protection

        self.retrieve = async_to_raw_response_wrapper(
            protection.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            protection.update,
        )
        self.delete = async_to_raw_response_wrapper(
            protection.delete,
        )

    @cached_property
    def enforce_admins(self) -> AsyncEnforceAdminsResourceWithRawResponse:
        return AsyncEnforceAdminsResourceWithRawResponse(self._protection.enforce_admins)

    @cached_property
    def required_pull_request_reviews(self) -> AsyncRequiredPullRequestReviewsResourceWithRawResponse:
        return AsyncRequiredPullRequestReviewsResourceWithRawResponse(self._protection.required_pull_request_reviews)

    @cached_property
    def required_signatures(self) -> AsyncRequiredSignaturesResourceWithRawResponse:
        return AsyncRequiredSignaturesResourceWithRawResponse(self._protection.required_signatures)

    @cached_property
    def required_status_checks(self) -> AsyncRequiredStatusChecksResourceWithRawResponse:
        return AsyncRequiredStatusChecksResourceWithRawResponse(self._protection.required_status_checks)

    @cached_property
    def restrictions(self) -> AsyncRestrictionsResourceWithRawResponse:
        return AsyncRestrictionsResourceWithRawResponse(self._protection.restrictions)


class ProtectionResourceWithStreamingResponse:
    def __init__(self, protection: ProtectionResource) -> None:
        self._protection = protection

        self.retrieve = to_streamed_response_wrapper(
            protection.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            protection.update,
        )
        self.delete = to_streamed_response_wrapper(
            protection.delete,
        )

    @cached_property
    def enforce_admins(self) -> EnforceAdminsResourceWithStreamingResponse:
        return EnforceAdminsResourceWithStreamingResponse(self._protection.enforce_admins)

    @cached_property
    def required_pull_request_reviews(self) -> RequiredPullRequestReviewsResourceWithStreamingResponse:
        return RequiredPullRequestReviewsResourceWithStreamingResponse(self._protection.required_pull_request_reviews)

    @cached_property
    def required_signatures(self) -> RequiredSignaturesResourceWithStreamingResponse:
        return RequiredSignaturesResourceWithStreamingResponse(self._protection.required_signatures)

    @cached_property
    def required_status_checks(self) -> RequiredStatusChecksResourceWithStreamingResponse:
        return RequiredStatusChecksResourceWithStreamingResponse(self._protection.required_status_checks)

    @cached_property
    def restrictions(self) -> RestrictionsResourceWithStreamingResponse:
        return RestrictionsResourceWithStreamingResponse(self._protection.restrictions)


class AsyncProtectionResourceWithStreamingResponse:
    def __init__(self, protection: AsyncProtectionResource) -> None:
        self._protection = protection

        self.retrieve = async_to_streamed_response_wrapper(
            protection.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            protection.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            protection.delete,
        )

    @cached_property
    def enforce_admins(self) -> AsyncEnforceAdminsResourceWithStreamingResponse:
        return AsyncEnforceAdminsResourceWithStreamingResponse(self._protection.enforce_admins)

    @cached_property
    def required_pull_request_reviews(self) -> AsyncRequiredPullRequestReviewsResourceWithStreamingResponse:
        return AsyncRequiredPullRequestReviewsResourceWithStreamingResponse(self._protection.required_pull_request_reviews)

    @cached_property
    def required_signatures(self) -> AsyncRequiredSignaturesResourceWithStreamingResponse:
        return AsyncRequiredSignaturesResourceWithStreamingResponse(self._protection.required_signatures)

    @cached_property
    def required_status_checks(self) -> AsyncRequiredStatusChecksResourceWithStreamingResponse:
        return AsyncRequiredStatusChecksResourceWithStreamingResponse(self._protection.required_status_checks)

    @cached_property
    def restrictions(self) -> AsyncRestrictionsResourceWithStreamingResponse:
        return AsyncRestrictionsResourceWithStreamingResponse(self._protection.restrictions)
