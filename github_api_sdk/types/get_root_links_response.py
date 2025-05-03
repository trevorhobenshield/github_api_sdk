

from typing import Optional

from .._models import BaseModel

__all__ = ["GetRootLinksResponse"]


class GetRootLinksResponse(BaseModel):
    authorizations_url: str

    code_search_url: str

    commit_search_url: str

    current_user_authorizations_html_url: str

    current_user_repositories_url: str

    current_user_url: str

    emails_url: str

    emojis_url: str

    events_url: str

    feeds_url: str

    followers_url: str

    following_url: str

    gists_url: str

    issue_search_url: str

    issues_url: str

    keys_url: str

    label_search_url: str

    notifications_url: str

    organization_repositories_url: str

    organization_teams_url: str

    organization_url: str

    public_gists_url: str

    rate_limit_url: str

    repository_search_url: str

    repository_url: str

    starred_gists_url: str

    starred_url: str

    user_organizations_url: str

    user_repositories_url: str

    user_search_url: str

    user_url: str

    hub_url: Optional[str] = None

    topic_search_url: Optional[str] = None
