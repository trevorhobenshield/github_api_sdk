


from .ruleset_version import RulesetVersion

__all__ = ["RulesetVersionWithState"]


class RulesetVersionWithState(RulesetVersion):
    state: object
    """The state of the ruleset version"""
