

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import (
    zen,
    meta,
    feeds,
    emojis,
    events,
    issues,
    octocat,
    licenses,
    markdown,
    networks,
    advisories,
    classrooms,
    rate_limit,
    assignments,
    installation,
    repositories,
    app_manifests,
    codes_of_conduct,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .resources.orgs import orgs
from .resources.gists import gists
from .resources.repos import repos
from .resources.teams import teams
from .resources.users import users
from .resources.search import search
from .resources.projects import projects
from .resources.gitignore import gitignore
from .resources.enterprises import enterprises
from .resources.applications import applications
from .resources.notifications import notifications
from .resources.organizations import organizations
from .resources.marketplace_listing import marketplace_listing
from .types.get_root_links_response import GetRootLinksResponse

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "GitHubAPI",
    "AsyncGitHubAPI",
    "Client",
    "AsyncClient",
]


class GitHubAPI(SyncAPIClient):
    advisories: advisories.AdvisoriesResource
    app_manifests: app_manifests.AppManifestsResource
    applications: applications.ApplicationsResource
    assignments: assignments.AssignmentsResource
    classrooms: classrooms.ClassroomsResource
    codes_of_conduct: codes_of_conduct.CodesOfConductResource
    emojis: emojis.EmojisResource
    enterprises: enterprises.EnterprisesResource
    events: events.EventsResource
    feeds: feeds.FeedsResource
    gists: gists.GistsResource
    gitignore: gitignore.GitignoreResource
    installation: installation.InstallationResource
    issues: issues.IssuesResource
    licenses: licenses.LicensesResource
    markdown: markdown.MarkdownResource
    marketplace_listing: marketplace_listing.MarketplaceListingResource
    meta: meta.MetaResource
    networks: networks.NetworksResource
    notifications: notifications.NotificationsResource
    octocat: octocat.OctocatResource
    organizations: organizations.OrganizationsResource
    orgs: orgs.OrgsResource
    projects: projects.ProjectsResource
    rate_limit: rate_limit.RateLimitResource
    repos: repos.ReposResource
    repositories: repositories.RepositoriesResource
    search: search.SearchResource
    teams: teams.TeamsResource
    zen: zen.ZenResource
    users: users.UsersResource
    with_raw_response: GitHubAPIWithRawResponse
    with_streaming_response: GitHubAPIWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous GitHubAPI client instance.

        This automatically infers the `api_key` argument from the `GITHUB_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("GITHUB_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("GITHUBAPI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.github.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.advisories = advisories.AdvisoriesResource(self)
        self.app_manifests = app_manifests.AppManifestsResource(self)
        self.applications = applications.ApplicationsResource(self)
        self.assignments = assignments.AssignmentsResource(self)
        self.classrooms = classrooms.ClassroomsResource(self)
        self.codes_of_conduct = codes_of_conduct.CodesOfConductResource(self)
        self.emojis = emojis.EmojisResource(self)
        self.enterprises = enterprises.EnterprisesResource(self)
        self.events = events.EventsResource(self)
        self.feeds = feeds.FeedsResource(self)
        self.gists = gists.GistsResource(self)
        self.gitignore = gitignore.GitignoreResource(self)
        self.installation = installation.InstallationResource(self)
        self.issues = issues.IssuesResource(self)
        self.licenses = licenses.LicensesResource(self)
        self.markdown = markdown.MarkdownResource(self)
        self.marketplace_listing = marketplace_listing.MarketplaceListingResource(self)
        self.meta = meta.MetaResource(self)
        self.networks = networks.NetworksResource(self)
        self.notifications = notifications.NotificationsResource(self)
        self.octocat = octocat.OctocatResource(self)
        self.organizations = organizations.OrganizationsResource(self)
        self.orgs = orgs.OrgsResource(self)
        self.projects = projects.ProjectsResource(self)
        self.rate_limit = rate_limit.RateLimitResource(self)
        self.repos = repos.ReposResource(self)
        self.repositories = repositories.RepositoriesResource(self)
        self.search = search.SearchResource(self)
        self.teams = teams.TeamsResource(self)
        self.zen = zen.ZenResource(self)
        self.users = users.UsersResource(self)
        self.with_raw_response = GitHubAPIWithRawResponse(self)
        self.with_streaming_response = GitHubAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def get_root_links(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetRootLinksResponse:
        """Get Hypermedia links to resources accessible in GitHub's REST API"""
        return self.get(
            "/",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GetRootLinksResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncGitHubAPI(AsyncAPIClient):
    advisories: advisories.AsyncAdvisoriesResource
    app_manifests: app_manifests.AsyncAppManifestsResource
    applications: applications.AsyncApplicationsResource
    assignments: assignments.AsyncAssignmentsResource
    classrooms: classrooms.AsyncClassroomsResource
    codes_of_conduct: codes_of_conduct.AsyncCodesOfConductResource
    emojis: emojis.AsyncEmojisResource
    enterprises: enterprises.AsyncEnterprisesResource
    events: events.AsyncEventsResource
    feeds: feeds.AsyncFeedsResource
    gists: gists.AsyncGistsResource
    gitignore: gitignore.AsyncGitignoreResource
    installation: installation.AsyncInstallationResource
    issues: issues.AsyncIssuesResource
    licenses: licenses.AsyncLicensesResource
    markdown: markdown.AsyncMarkdownResource
    marketplace_listing: marketplace_listing.AsyncMarketplaceListingResource
    meta: meta.AsyncMetaResource
    networks: networks.AsyncNetworksResource
    notifications: notifications.AsyncNotificationsResource
    octocat: octocat.AsyncOctocatResource
    organizations: organizations.AsyncOrganizationsResource
    orgs: orgs.AsyncOrgsResource
    projects: projects.AsyncProjectsResource
    rate_limit: rate_limit.AsyncRateLimitResource
    repos: repos.AsyncReposResource
    repositories: repositories.AsyncRepositoriesResource
    search: search.AsyncSearchResource
    teams: teams.AsyncTeamsResource
    zen: zen.AsyncZenResource
    users: users.AsyncUsersResource
    with_raw_response: AsyncGitHubAPIWithRawResponse
    with_streaming_response: AsyncGitHubAPIWithStreamedResponse

    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncGitHubAPI client instance.

        This automatically infers the `api_key` argument from the `GITHUB_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("GITHUB_API_KEY")
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("GITHUBAPI_BASE_URL")
        if base_url is None:
            base_url = f"https://api.github.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.advisories = advisories.AsyncAdvisoriesResource(self)
        self.app_manifests = app_manifests.AsyncAppManifestsResource(self)
        self.applications = applications.AsyncApplicationsResource(self)
        self.assignments = assignments.AsyncAssignmentsResource(self)
        self.classrooms = classrooms.AsyncClassroomsResource(self)
        self.codes_of_conduct = codes_of_conduct.AsyncCodesOfConductResource(self)
        self.emojis = emojis.AsyncEmojisResource(self)
        self.enterprises = enterprises.AsyncEnterprisesResource(self)
        self.events = events.AsyncEventsResource(self)
        self.feeds = feeds.AsyncFeedsResource(self)
        self.gists = gists.AsyncGistsResource(self)
        self.gitignore = gitignore.AsyncGitignoreResource(self)
        self.installation = installation.AsyncInstallationResource(self)
        self.issues = issues.AsyncIssuesResource(self)
        self.licenses = licenses.AsyncLicensesResource(self)
        self.markdown = markdown.AsyncMarkdownResource(self)
        self.marketplace_listing = marketplace_listing.AsyncMarketplaceListingResource(self)
        self.meta = meta.AsyncMetaResource(self)
        self.networks = networks.AsyncNetworksResource(self)
        self.notifications = notifications.AsyncNotificationsResource(self)
        self.octocat = octocat.AsyncOctocatResource(self)
        self.organizations = organizations.AsyncOrganizationsResource(self)
        self.orgs = orgs.AsyncOrgsResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.rate_limit = rate_limit.AsyncRateLimitResource(self)
        self.repos = repos.AsyncReposResource(self)
        self.repositories = repositories.AsyncRepositoriesResource(self)
        self.search = search.AsyncSearchResource(self)
        self.teams = teams.AsyncTeamsResource(self)
        self.zen = zen.AsyncZenResource(self)
        self.users = users.AsyncUsersResource(self)
        self.with_raw_response = AsyncGitHubAPIWithRawResponse(self)
        self.with_streaming_response = AsyncGitHubAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.api_key and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    async def get_root_links(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetRootLinksResponse:
        """Get Hypermedia links to resources accessible in GitHub's REST API"""
        return await self.get(
            "/",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GetRootLinksResponse,
        )

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class GitHubAPIWithRawResponse:
    def __init__(self, client: GitHubAPI) -> None:
        self.advisories = advisories.AdvisoriesResourceWithRawResponse(client.advisories)
        self.app_manifests = app_manifests.AppManifestsResourceWithRawResponse(client.app_manifests)
        self.applications = applications.ApplicationsResourceWithRawResponse(client.applications)
        self.assignments = assignments.AssignmentsResourceWithRawResponse(client.assignments)
        self.classrooms = classrooms.ClassroomsResourceWithRawResponse(client.classrooms)
        self.codes_of_conduct = codes_of_conduct.CodesOfConductResourceWithRawResponse(client.codes_of_conduct)
        self.emojis = emojis.EmojisResourceWithRawResponse(client.emojis)
        self.enterprises = enterprises.EnterprisesResourceWithRawResponse(client.enterprises)
        self.events = events.EventsResourceWithRawResponse(client.events)
        self.feeds = feeds.FeedsResourceWithRawResponse(client.feeds)
        self.gists = gists.GistsResourceWithRawResponse(client.gists)
        self.gitignore = gitignore.GitignoreResourceWithRawResponse(client.gitignore)
        self.installation = installation.InstallationResourceWithRawResponse(client.installation)
        self.issues = issues.IssuesResourceWithRawResponse(client.issues)
        self.licenses = licenses.LicensesResourceWithRawResponse(client.licenses)
        self.markdown = markdown.MarkdownResourceWithRawResponse(client.markdown)
        self.marketplace_listing = marketplace_listing.MarketplaceListingResourceWithRawResponse(client.marketplace_listing)
        self.meta = meta.MetaResourceWithRawResponse(client.meta)
        self.networks = networks.NetworksResourceWithRawResponse(client.networks)
        self.notifications = notifications.NotificationsResourceWithRawResponse(client.notifications)
        self.octocat = octocat.OctocatResourceWithRawResponse(client.octocat)
        self.organizations = organizations.OrganizationsResourceWithRawResponse(client.organizations)
        self.orgs = orgs.OrgsResourceWithRawResponse(client.orgs)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.rate_limit = rate_limit.RateLimitResourceWithRawResponse(client.rate_limit)
        self.repos = repos.ReposResourceWithRawResponse(client.repos)
        self.repositories = repositories.RepositoriesResourceWithRawResponse(client.repositories)
        self.search = search.SearchResourceWithRawResponse(client.search)
        self.teams = teams.TeamsResourceWithRawResponse(client.teams)
        self.zen = zen.ZenResourceWithRawResponse(client.zen)
        self.users = users.UsersResourceWithRawResponse(client.users)

        self.get_root_links = to_raw_response_wrapper(
            client.get_root_links,
        )


class AsyncGitHubAPIWithRawResponse:
    def __init__(self, client: AsyncGitHubAPI) -> None:
        self.advisories = advisories.AsyncAdvisoriesResourceWithRawResponse(client.advisories)
        self.app_manifests = app_manifests.AsyncAppManifestsResourceWithRawResponse(client.app_manifests)
        self.applications = applications.AsyncApplicationsResourceWithRawResponse(client.applications)
        self.assignments = assignments.AsyncAssignmentsResourceWithRawResponse(client.assignments)
        self.classrooms = classrooms.AsyncClassroomsResourceWithRawResponse(client.classrooms)
        self.codes_of_conduct = codes_of_conduct.AsyncCodesOfConductResourceWithRawResponse(client.codes_of_conduct)
        self.emojis = emojis.AsyncEmojisResourceWithRawResponse(client.emojis)
        self.enterprises = enterprises.AsyncEnterprisesResourceWithRawResponse(client.enterprises)
        self.events = events.AsyncEventsResourceWithRawResponse(client.events)
        self.feeds = feeds.AsyncFeedsResourceWithRawResponse(client.feeds)
        self.gists = gists.AsyncGistsResourceWithRawResponse(client.gists)
        self.gitignore = gitignore.AsyncGitignoreResourceWithRawResponse(client.gitignore)
        self.installation = installation.AsyncInstallationResourceWithRawResponse(client.installation)
        self.issues = issues.AsyncIssuesResourceWithRawResponse(client.issues)
        self.licenses = licenses.AsyncLicensesResourceWithRawResponse(client.licenses)
        self.markdown = markdown.AsyncMarkdownResourceWithRawResponse(client.markdown)
        self.marketplace_listing = marketplace_listing.AsyncMarketplaceListingResourceWithRawResponse(client.marketplace_listing)
        self.meta = meta.AsyncMetaResourceWithRawResponse(client.meta)
        self.networks = networks.AsyncNetworksResourceWithRawResponse(client.networks)
        self.notifications = notifications.AsyncNotificationsResourceWithRawResponse(client.notifications)
        self.octocat = octocat.AsyncOctocatResourceWithRawResponse(client.octocat)
        self.organizations = organizations.AsyncOrganizationsResourceWithRawResponse(client.organizations)
        self.orgs = orgs.AsyncOrgsResourceWithRawResponse(client.orgs)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.rate_limit = rate_limit.AsyncRateLimitResourceWithRawResponse(client.rate_limit)
        self.repos = repos.AsyncReposResourceWithRawResponse(client.repos)
        self.repositories = repositories.AsyncRepositoriesResourceWithRawResponse(client.repositories)
        self.search = search.AsyncSearchResourceWithRawResponse(client.search)
        self.teams = teams.AsyncTeamsResourceWithRawResponse(client.teams)
        self.zen = zen.AsyncZenResourceWithRawResponse(client.zen)
        self.users = users.AsyncUsersResourceWithRawResponse(client.users)

        self.get_root_links = async_to_raw_response_wrapper(
            client.get_root_links,
        )


class GitHubAPIWithStreamedResponse:
    def __init__(self, client: GitHubAPI) -> None:
        self.advisories = advisories.AdvisoriesResourceWithStreamingResponse(client.advisories)
        self.app_manifests = app_manifests.AppManifestsResourceWithStreamingResponse(client.app_manifests)
        self.applications = applications.ApplicationsResourceWithStreamingResponse(client.applications)
        self.assignments = assignments.AssignmentsResourceWithStreamingResponse(client.assignments)
        self.classrooms = classrooms.ClassroomsResourceWithStreamingResponse(client.classrooms)
        self.codes_of_conduct = codes_of_conduct.CodesOfConductResourceWithStreamingResponse(client.codes_of_conduct)
        self.emojis = emojis.EmojisResourceWithStreamingResponse(client.emojis)
        self.enterprises = enterprises.EnterprisesResourceWithStreamingResponse(client.enterprises)
        self.events = events.EventsResourceWithStreamingResponse(client.events)
        self.feeds = feeds.FeedsResourceWithStreamingResponse(client.feeds)
        self.gists = gists.GistsResourceWithStreamingResponse(client.gists)
        self.gitignore = gitignore.GitignoreResourceWithStreamingResponse(client.gitignore)
        self.installation = installation.InstallationResourceWithStreamingResponse(client.installation)
        self.issues = issues.IssuesResourceWithStreamingResponse(client.issues)
        self.licenses = licenses.LicensesResourceWithStreamingResponse(client.licenses)
        self.markdown = markdown.MarkdownResourceWithStreamingResponse(client.markdown)
        self.marketplace_listing = marketplace_listing.MarketplaceListingResourceWithStreamingResponse(client.marketplace_listing)
        self.meta = meta.MetaResourceWithStreamingResponse(client.meta)
        self.networks = networks.NetworksResourceWithStreamingResponse(client.networks)
        self.notifications = notifications.NotificationsResourceWithStreamingResponse(client.notifications)
        self.octocat = octocat.OctocatResourceWithStreamingResponse(client.octocat)
        self.organizations = organizations.OrganizationsResourceWithStreamingResponse(client.organizations)
        self.orgs = orgs.OrgsResourceWithStreamingResponse(client.orgs)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.rate_limit = rate_limit.RateLimitResourceWithStreamingResponse(client.rate_limit)
        self.repos = repos.ReposResourceWithStreamingResponse(client.repos)
        self.repositories = repositories.RepositoriesResourceWithStreamingResponse(client.repositories)
        self.search = search.SearchResourceWithStreamingResponse(client.search)
        self.teams = teams.TeamsResourceWithStreamingResponse(client.teams)
        self.zen = zen.ZenResourceWithStreamingResponse(client.zen)
        self.users = users.UsersResourceWithStreamingResponse(client.users)

        self.get_root_links = to_streamed_response_wrapper(
            client.get_root_links,
        )


class AsyncGitHubAPIWithStreamedResponse:
    def __init__(self, client: AsyncGitHubAPI) -> None:
        self.advisories = advisories.AsyncAdvisoriesResourceWithStreamingResponse(client.advisories)
        self.app_manifests = app_manifests.AsyncAppManifestsResourceWithStreamingResponse(client.app_manifests)
        self.applications = applications.AsyncApplicationsResourceWithStreamingResponse(client.applications)
        self.assignments = assignments.AsyncAssignmentsResourceWithStreamingResponse(client.assignments)
        self.classrooms = classrooms.AsyncClassroomsResourceWithStreamingResponse(client.classrooms)
        self.codes_of_conduct = codes_of_conduct.AsyncCodesOfConductResourceWithStreamingResponse(client.codes_of_conduct)
        self.emojis = emojis.AsyncEmojisResourceWithStreamingResponse(client.emojis)
        self.enterprises = enterprises.AsyncEnterprisesResourceWithStreamingResponse(client.enterprises)
        self.events = events.AsyncEventsResourceWithStreamingResponse(client.events)
        self.feeds = feeds.AsyncFeedsResourceWithStreamingResponse(client.feeds)
        self.gists = gists.AsyncGistsResourceWithStreamingResponse(client.gists)
        self.gitignore = gitignore.AsyncGitignoreResourceWithStreamingResponse(client.gitignore)
        self.installation = installation.AsyncInstallationResourceWithStreamingResponse(client.installation)
        self.issues = issues.AsyncIssuesResourceWithStreamingResponse(client.issues)
        self.licenses = licenses.AsyncLicensesResourceWithStreamingResponse(client.licenses)
        self.markdown = markdown.AsyncMarkdownResourceWithStreamingResponse(client.markdown)
        self.marketplace_listing = marketplace_listing.AsyncMarketplaceListingResourceWithStreamingResponse(client.marketplace_listing)
        self.meta = meta.AsyncMetaResourceWithStreamingResponse(client.meta)
        self.networks = networks.AsyncNetworksResourceWithStreamingResponse(client.networks)
        self.notifications = notifications.AsyncNotificationsResourceWithStreamingResponse(client.notifications)
        self.octocat = octocat.AsyncOctocatResourceWithStreamingResponse(client.octocat)
        self.organizations = organizations.AsyncOrganizationsResourceWithStreamingResponse(client.organizations)
        self.orgs = orgs.AsyncOrgsResourceWithStreamingResponse(client.orgs)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.rate_limit = rate_limit.AsyncRateLimitResourceWithStreamingResponse(client.rate_limit)
        self.repos = repos.AsyncReposResourceWithStreamingResponse(client.repos)
        self.repositories = repositories.AsyncRepositoriesResourceWithStreamingResponse(client.repositories)
        self.search = search.AsyncSearchResourceWithStreamingResponse(client.search)
        self.teams = teams.AsyncTeamsResourceWithStreamingResponse(client.teams)
        self.zen = zen.AsyncZenResourceWithStreamingResponse(client.zen)
        self.users = users.AsyncUsersResourceWithStreamingResponse(client.users)

        self.get_root_links = async_to_streamed_response_wrapper(
            client.get_root_links,
        )


Client = GitHubAPI

AsyncClient = AsyncGitHubAPI
