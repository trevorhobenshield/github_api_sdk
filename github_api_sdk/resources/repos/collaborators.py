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
from ..._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.repos import collaborator_add_params, collaborator_list_params
from ...types.repos.collaborator_get_permission_response import CollaboratorGetPermissionResponse
from ...types.repos.collaborator_list_response import CollaboratorListResponse
from ...types.repos.repository_invitation import RepositoryInvitation

__all__ = ["CollaboratorsResource", "AsyncCollaboratorsResource"]


class CollaboratorsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollaboratorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CollaboratorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollaboratorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CollaboratorsResourceWithStreamingResponse(self)

    def list(
        self,
        repo: str,
        *,
        owner: str,
        affiliation: Literal["outside", "direct", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        permission: Literal["pull", "triage", "push", "maintain", "admin"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollaboratorListResponse:
        """
        For organization-owned repositories, the list of collaborators includes outside
        collaborators, organization members that are direct collaborators, organization
        members with access through team memberships, organization members with access
        through default organization permissions, and organization owners. Organization
        members with write, maintain, or admin privileges on the organization-owned
        repository can use this endpoint.

        Team members will include the members of child teams.

        The authenticated user must have push access to the repository to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `read:org` and
        `repo` scopes to use this endpoint.

        Args:
          affiliation: Filter collaborators returned by their affiliation. `outside` means all outside
              collaborators of an organization-owned repository. `direct` means all
              collaborators with permissions to an organization-owned repository, regardless
              of organization membership status. `all` means all collaborators the
              authenticated user can see.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          permission: Filter collaborators by the permissions they have on the repository. If not
              specified, all collaborators will be returned.

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
            f"/repos/{owner}/{repo}/collaborators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "affiliation": affiliation,
                        "page": page,
                        "per_page": per_page,
                        "permission": permission,
                    },
                    collaborator_list_params.CollaboratorListParams,
                ),
            ),
            cast_to=CollaboratorListResponse,
        )

    def add(
        self,
        username: str,
        *,
        owner: str,
        repo: str,
        permission: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryInvitation:
        """
        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Adding an outside collaborator may be restricted by enterprise administrators.
        For more information, see
        "[Enforcing repository management policies in your enterprise](https://docs.github.com/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#enforcing-a-policy-for-inviting-outside-collaborators-to-repositories)."

        For more information on permission levels, see
        "[Repository permission levels for an organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)".
        There are restrictions on which permissions can be granted to organization
        members when an organization base role is in place. In this case, the permission
        being given must be equal to or higher than the org base permission. Otherwise,
        the request will fail with:

        ```
        Cannot assign {member} permission of {role name}
        ```

        Note that, if you choose not to pass any parameters, you'll need to set
        `Content-Length` to zero when calling out to this endpoint. For more
        information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        The invitee will receive a notification that they have been invited to the
        repository, which they must accept or decline. They may do this via the
        notifications page, the email they receive, or by using the
        [API](https://docs.github.com/rest/collaborators/invitations).

        **Updating an existing collaborator's permission level**

        The endpoint can also be used to change the permissions of an existing
        collaborator without first removing and re-adding the collaborator. To change
        the permissions, use the same endpoint and pass a different `permission`
        parameter. The response will be a `204`, with no other indication that the
        permission level changed.

        **Rate limits**

        You are limited to sending 50 invitations to a repository per 24 hour period.
        Note there is no limit if you are inviting organization members to an
        organization repository.

        Args:
          permission: The permission to grant the collaborator. **Only valid on organization-owned
              repositories.** We accept the following permissions to be set: `pull`, `triage`,
              `push`, `maintain`, `admin` and you can also specify a custom repository role
              name, if the owning organization has defined any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._put(
            f"/repos/{owner}/{repo}/collaborators/{username}",
            body=maybe_transform({"permission": permission}, collaborator_add_params.CollaboratorAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryInvitation,
        )

    def check(
        self,
        username: str,
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
        For organization-owned repositories, the list of collaborators includes outside
        collaborators, organization members that are direct collaborators, organization
        members with access through team memberships, organization members with access
        through default organization permissions, and organization owners.

        Team members will include the members of child teams.

        The authenticated user must have push access to the repository to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `read:org` and
        `repo` scopes to use this endpoint.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/repos/{owner}/{repo}/collaborators/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def get_permission(
        self,
        username: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollaboratorGetPermissionResponse:
        """Checks the repository permission of a collaborator.

        The possible repository
        permissions are `admin`, `write`, `read`, and `none`.

        _Note_: The `permission` attribute provides the legacy base roles of `admin`,
        `write`, `read`, and `none`, where the `maintain` role is mapped to `write` and
        the `triage` role is mapped to `read`. To determine the role assigned to the
        collaborator, see the `role_name` attribute, which will provide the full role
        name, including custom roles. The `permissions` hash can also be used to
        determine which base level of access the collaborator has to the repository.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return self._get(
            f"/repos/{owner}/{repo}/collaborators/{username}/permission",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CollaboratorGetPermissionResponse,
        )

    def remove(
        self,
        username: str,
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
        Removes a collaborator from a repository.

        To use this endpoint, the authenticated user must either be an administrator of
        the repository or target themselves for removal.

        This endpoint also:

        - Cancels any outstanding invitations sent by the collaborator
        - Unassigns the user from any issues
        - Removes access to organization projects if the user is not an organization
          member and is not a collaborator on any other organization repositories.
        - Unstars the repository
        - Updates access permissions to packages

        Removing a user as a collaborator has the following effects on forks:

        - If the user had access to a fork through their membership to this repository,
          the user will also be removed from the fork.
        - If the user had their own fork of the repository, the fork will be deleted.
        - If the user still has read access to the repository, open pull requests by
          this user from a fork will be denied.

        > [!NOTE] A user can still have access to the repository through organization
        > permissions like base repository permissions.

        Although the API responds immediately, the additional permission updates might
        take some extra time to complete in the background.

        For more information on fork permissions, see
        "[About permissions and visibility of forks](https://docs.github.com/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks)".

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/collaborators/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncCollaboratorsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollaboratorsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollaboratorsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollaboratorsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCollaboratorsResourceWithStreamingResponse(self)

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        affiliation: Literal["outside", "direct", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        permission: Literal["pull", "triage", "push", "maintain", "admin"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollaboratorListResponse:
        """
        For organization-owned repositories, the list of collaborators includes outside
        collaborators, organization members that are direct collaborators, organization
        members with access through team memberships, organization members with access
        through default organization permissions, and organization owners. Organization
        members with write, maintain, or admin privileges on the organization-owned
        repository can use this endpoint.

        Team members will include the members of child teams.

        The authenticated user must have push access to the repository to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `read:org` and
        `repo` scopes to use this endpoint.

        Args:
          affiliation: Filter collaborators returned by their affiliation. `outside` means all outside
              collaborators of an organization-owned repository. `direct` means all
              collaborators with permissions to an organization-owned repository, regardless
              of organization membership status. `all` means all collaborators the
              authenticated user can see.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          permission: Filter collaborators by the permissions they have on the repository. If not
              specified, all collaborators will be returned.

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
            f"/repos/{owner}/{repo}/collaborators",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "affiliation": affiliation,
                        "page": page,
                        "per_page": per_page,
                        "permission": permission,
                    },
                    collaborator_list_params.CollaboratorListParams,
                ),
            ),
            cast_to=CollaboratorListResponse,
        )

    async def add(
        self,
        username: str,
        *,
        owner: str,
        repo: str,
        permission: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepositoryInvitation:
        """
        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Adding an outside collaborator may be restricted by enterprise administrators.
        For more information, see
        "[Enforcing repository management policies in your enterprise](https://docs.github.com/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#enforcing-a-policy-for-inviting-outside-collaborators-to-repositories)."

        For more information on permission levels, see
        "[Repository permission levels for an organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)".
        There are restrictions on which permissions can be granted to organization
        members when an organization base role is in place. In this case, the permission
        being given must be equal to or higher than the org base permission. Otherwise,
        the request will fail with:

        ```
        Cannot assign {member} permission of {role name}
        ```

        Note that, if you choose not to pass any parameters, you'll need to set
        `Content-Length` to zero when calling out to this endpoint. For more
        information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        The invitee will receive a notification that they have been invited to the
        repository, which they must accept or decline. They may do this via the
        notifications page, the email they receive, or by using the
        [API](https://docs.github.com/rest/collaborators/invitations).

        **Updating an existing collaborator's permission level**

        The endpoint can also be used to change the permissions of an existing
        collaborator without first removing and re-adding the collaborator. To change
        the permissions, use the same endpoint and pass a different `permission`
        parameter. The response will be a `204`, with no other indication that the
        permission level changed.

        **Rate limits**

        You are limited to sending 50 invitations to a repository per 24 hour period.
        Note there is no limit if you are inviting organization members to an
        organization repository.

        Args:
          permission: The permission to grant the collaborator. **Only valid on organization-owned
              repositories.** We accept the following permissions to be set: `pull`, `triage`,
              `push`, `maintain`, `admin` and you can also specify a custom repository role
              name, if the owning organization has defined any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/collaborators/{username}",
            body=await async_maybe_transform({"permission": permission}, collaborator_add_params.CollaboratorAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=RepositoryInvitation,
        )

    async def check(
        self,
        username: str,
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
        For organization-owned repositories, the list of collaborators includes outside
        collaborators, organization members that are direct collaborators, organization
        members with access through team memberships, organization members with access
        through default organization permissions, and organization owners.

        Team members will include the members of child teams.

        The authenticated user must have push access to the repository to use this
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `read:org` and
        `repo` scopes to use this endpoint.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/repos/{owner}/{repo}/collaborators/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def get_permission(
        self,
        username: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollaboratorGetPermissionResponse:
        """Checks the repository permission of a collaborator.

        The possible repository
        permissions are `admin`, `write`, `read`, and `none`.

        _Note_: The `permission` attribute provides the legacy base roles of `admin`,
        `write`, `read`, and `none`, where the `maintain` role is mapped to `write` and
        the `triage` role is mapped to `read`. To determine the role assigned to the
        collaborator, see the `role_name` attribute, which will provide the full role
        name, including custom roles. The `permissions` hash can also be used to
        determine which base level of access the collaborator has to the repository.

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/collaborators/{username}/permission",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CollaboratorGetPermissionResponse,
        )

    async def remove(
        self,
        username: str,
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
        Removes a collaborator from a repository.

        To use this endpoint, the authenticated user must either be an administrator of
        the repository or target themselves for removal.

        This endpoint also:

        - Cancels any outstanding invitations sent by the collaborator
        - Unassigns the user from any issues
        - Removes access to organization projects if the user is not an organization
          member and is not a collaborator on any other organization repositories.
        - Unstars the repository
        - Updates access permissions to packages

        Removing a user as a collaborator has the following effects on forks:

        - If the user had access to a fork through their membership to this repository,
          the user will also be removed from the fork.
        - If the user had their own fork of the repository, the fork will be deleted.
        - If the user still has read access to the repository, open pull requests by
          this user from a fork will be denied.

        > [!NOTE] A user can still have access to the repository through organization
        > permissions like base repository permissions.

        Although the API responds immediately, the additional permission updates might
        take some extra time to complete in the background.

        For more information on fork permissions, see
        "[About permissions and visibility of forks](https://docs.github.com/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks)".

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
        if not username:
            raise ValueError(f"Expected a non-empty value for `username` but received {username!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/collaborators/{username}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class CollaboratorsResourceWithRawResponse:
    def __init__(self, collaborators: CollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = to_raw_response_wrapper(
            collaborators.list,
        )
        self.add = to_raw_response_wrapper(
            collaborators.add,
        )
        self.check = to_raw_response_wrapper(
            collaborators.check,
        )
        self.get_permission = to_raw_response_wrapper(
            collaborators.get_permission,
        )
        self.remove = to_raw_response_wrapper(
            collaborators.remove,
        )


class AsyncCollaboratorsResourceWithRawResponse:
    def __init__(self, collaborators: AsyncCollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = async_to_raw_response_wrapper(
            collaborators.list,
        )
        self.add = async_to_raw_response_wrapper(
            collaborators.add,
        )
        self.check = async_to_raw_response_wrapper(
            collaborators.check,
        )
        self.get_permission = async_to_raw_response_wrapper(
            collaborators.get_permission,
        )
        self.remove = async_to_raw_response_wrapper(
            collaborators.remove,
        )


class CollaboratorsResourceWithStreamingResponse:
    def __init__(self, collaborators: CollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = to_streamed_response_wrapper(
            collaborators.list,
        )
        self.add = to_streamed_response_wrapper(
            collaborators.add,
        )
        self.check = to_streamed_response_wrapper(
            collaborators.check,
        )
        self.get_permission = to_streamed_response_wrapper(
            collaborators.get_permission,
        )
        self.remove = to_streamed_response_wrapper(
            collaborators.remove,
        )


class AsyncCollaboratorsResourceWithStreamingResponse:
    def __init__(self, collaborators: AsyncCollaboratorsResource) -> None:
        self._collaborators = collaborators

        self.list = async_to_streamed_response_wrapper(
            collaborators.list,
        )
        self.add = async_to_streamed_response_wrapper(
            collaborators.add,
        )
        self.check = async_to_streamed_response_wrapper(
            collaborators.check,
        )
        self.get_permission = async_to_streamed_response_wrapper(
            collaborators.get_permission,
        )
        self.remove = async_to_streamed_response_wrapper(
            collaborators.remove,
        )
