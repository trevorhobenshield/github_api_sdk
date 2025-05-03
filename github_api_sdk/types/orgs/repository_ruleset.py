

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .repository_rule import RepositoryRule
from .repository_rule_enforcement import RepositoryRuleEnforcement
from .repository_ruleset_bypass_actor import RepositoryRulesetBypassActor
from ..repos.repository_ruleset_conditions import RepositoryRulesetConditions
from .repository_ruleset_conditions_repository_property_spec import RepositoryRulesetConditionsRepositoryPropertySpec

__all__ = [
    "RepositoryRuleset",
    "_Links",
    "_LinksHTML",
    "_LinksSelf",
    "Conditions",
    "ConditionsRepositoryNameAndRefName",
    "ConditionsRepositoryNameAndRefNameRepositoryName",
    "ConditionsRepositoryIDAndRefName",
    "ConditionsRepositoryIDAndRefNameRepositoryID",
    "ConditionsRepositoryPropertyAndRefName",
    "ConditionsRepositoryPropertyAndRefNameRepositoryProperty",
]


class _LinksHTML(BaseModel):
    href: Optional[str] = None
    """The html URL of the ruleset"""


class _LinksSelf(BaseModel):
    href: Optional[str] = None
    """The URL of the ruleset"""


class _Links(BaseModel):
    html: Optional[_LinksHTML] = None

    self: Optional[_LinksSelf] = None


class ConditionsRepositoryNameAndRefNameRepositoryName(BaseModel):
    exclude: Optional[List[str]] = None
    """Array of repository names or patterns to exclude.

    The condition will not pass if any of these patterns match.
    """

    include: Optional[List[str]] = None
    """Array of repository names or patterns to include.

    One of these patterns must match for the condition to pass. Also accepts `~ALL`
    to include all repositories.
    """

    protected: Optional[bool] = None
    """Whether renaming of target repositories is prevented."""


class ConditionsRepositoryNameAndRefName(RepositoryRulesetConditions):
    repository_name: ConditionsRepositoryNameAndRefNameRepositoryName


class ConditionsRepositoryIDAndRefNameRepositoryID(BaseModel):
    repository_ids: Optional[List[int]] = None
    """The repository IDs that the ruleset applies to.

    One of these IDs must match for the condition to pass.
    """


class ConditionsRepositoryIDAndRefName(RepositoryRulesetConditions):
    repository_id: ConditionsRepositoryIDAndRefNameRepositoryID


class ConditionsRepositoryPropertyAndRefNameRepositoryProperty(BaseModel):
    exclude: Optional[List[RepositoryRulesetConditionsRepositoryPropertySpec]] = None
    """The repository properties and values to exclude.

    The condition will not pass if any of these properties match.
    """

    include: Optional[List[RepositoryRulesetConditionsRepositoryPropertySpec]] = None
    """The repository properties and values to include.

    All of these properties must match for the condition to pass.
    """


class ConditionsRepositoryPropertyAndRefName(RepositoryRulesetConditions):
    repository_property: ConditionsRepositoryPropertyAndRefNameRepositoryProperty


Conditions: TypeAlias = Union[
    RepositoryRulesetConditions,
    ConditionsRepositoryNameAndRefName,
    ConditionsRepositoryIDAndRefName,
    ConditionsRepositoryPropertyAndRefName,
    None,
]


class RepositoryRuleset(BaseModel):
    id: int
    """The ID of the ruleset"""

    enforcement: RepositoryRuleEnforcement
    """The enforcement level of the ruleset.

    `evaluate` allows admins to test rules before enforcing them. Admins can view
    insights on the Rule Insights page (`evaluate` is only available with GitHub
    Enterprise).
    """

    name: str
    """The name of the ruleset"""

    source: str
    """The name of the source"""

    api_links: Optional[_Links] = FieldInfo(alias="_links", default=None)

    bypass_actors: Optional[List[RepositoryRulesetBypassActor]] = None
    """The actors that can bypass the rules in this ruleset"""

    conditions: Optional[Conditions] = None
    """Parameters for a repository ruleset ref name condition"""

    created_at: Optional[datetime] = None

    current_user_can_bypass: Optional[Literal["always", "pull_requests_only", "never"]] = None
    """The bypass type of the user making the API request for this ruleset.

    This field is only returned when querying the repository-level endpoint.
    """

    node_id: Optional[str] = None

    rules: Optional[List[RepositoryRule]] = None

    source_type: Optional[Literal["Repository", "Organization", "Enterprise"]] = None
    """The type of the source of the ruleset"""

    target: Optional[Literal["branch", "tag", "push", "repository"]] = None
    """The target of the ruleset"""

    updated_at: Optional[datetime] = None
