from __future__ import annotations

from typing import List

import httpx

from ......_base_client import make_request_options
from ......_compat import cached_property
from ......_resource import AsyncAPIResource, SyncAPIResource
from ......_response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ......_types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ......_utils import (
    async_maybe_transform,
    maybe_transform,
)
from ......types.repos.branches.protection.restrictions import user_add_params, user_remove_params, user_set_params
from ......types.repos.branches.protection.restrictions.user_add_response import UserAddResponse
from ......types.repos.branches.protection.restrictions.user_remove_response import UserRemoveResponse
from ......types.repos.branches.protection.restrictions.user_retrieve_response import UserRetrieveResponse
from ......types.repos.branches.protection.restrictions.user_set_response import UserSetResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

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
    ) -> UserRetrieveResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Lists the people who have push access to this branch.

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
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=UserRetrieveResponse,
        )

    def add(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        users: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAddResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Grants the specified people push access for this branch.

        | Type    | Description                                                                                                                   |
        | ------- | ----------------------------------------------------------------------------------------------------------------------------- |
        | `array` | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

        Args:
          users: The username for users

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
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users",
            body=maybe_transform({"users": users}, user_add_params.UserAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=UserAddResponse,
        )

    def remove(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        users: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRemoveResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Removes the ability of a user to push to this branch.

        | Type    | Description                                                                                                                                   |
        | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
        | `array` | Usernames of the people who should no longer have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

        Args:
          users: The username for users

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
        return self._delete(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users",
            body=maybe_transform({"users": users}, user_remove_params.UserRemoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=UserRemoveResponse,
        )

    def set(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        users: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSetResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Replaces the list of people that have push access to this branch. This removes
        all people that previously had push access and grants push access to the new
        list of people.

        | Type    | Description                                                                                                                   |
        | ------- | ----------------------------------------------------------------------------------------------------------------------------- |
        | `array` | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

        Args:
          users: The username for users

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
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users",
            body=maybe_transform({"users": users}, user_set_params.UserSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=UserSetResponse,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

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
    ) -> UserRetrieveResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Lists the people who have push access to this branch.

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
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=UserRetrieveResponse,
        )

    async def add(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        users: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserAddResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Grants the specified people push access for this branch.

        | Type    | Description                                                                                                                   |
        | ------- | ----------------------------------------------------------------------------------------------------------------------------- |
        | `array` | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

        Args:
          users: The username for users

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
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users",
            body=await async_maybe_transform({"users": users}, user_add_params.UserAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=UserAddResponse,
        )

    async def remove(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        users: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRemoveResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Removes the ability of a user to push to this branch.

        | Type    | Description                                                                                                                                   |
        | ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
        | `array` | Usernames of the people who should no longer have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

        Args:
          users: The username for users

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
        return await self._delete(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users",
            body=await async_maybe_transform({"users": users}, user_remove_params.UserRemoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=UserRemoveResponse,
        )

    async def set(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        users: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserSetResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Replaces the list of people that have push access to this branch. This removes
        all people that previously had push access and grants push access to the new
        list of people.

        | Type    | Description                                                                                                                   |
        | ------- | ----------------------------------------------------------------------------------------------------------------------------- |
        | `array` | Usernames for people who can have push access. **Note**: The list of users, apps, and teams in total is limited to 100 items. |

        Args:
          users: The username for users

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
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users",
            body=await async_maybe_transform({"users": users}, user_set_params.UserSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=UserSetResponse,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_raw_response_wrapper(
            users.retrieve,
        )
        self.add = to_raw_response_wrapper(
            users.add,
        )
        self.remove = to_raw_response_wrapper(
            users.remove,
        )
        self.set = to_raw_response_wrapper(
            users.set,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_raw_response_wrapper(
            users.retrieve,
        )
        self.add = async_to_raw_response_wrapper(
            users.add,
        )
        self.remove = async_to_raw_response_wrapper(
            users.remove,
        )
        self.set = async_to_raw_response_wrapper(
            users.set,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.retrieve = to_streamed_response_wrapper(
            users.retrieve,
        )
        self.add = to_streamed_response_wrapper(
            users.add,
        )
        self.remove = to_streamed_response_wrapper(
            users.remove,
        )
        self.set = to_streamed_response_wrapper(
            users.set,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.retrieve = async_to_streamed_response_wrapper(
            users.retrieve,
        )
        self.add = async_to_streamed_response_wrapper(
            users.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            users.remove,
        )
        self.set = async_to_streamed_response_wrapper(
            users.set,
        )
