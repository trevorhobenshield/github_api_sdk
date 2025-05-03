# GitHub API

Fluent GitHub API generated from OpenAPI spec using [Stainless](https://github.com/stainless-api) with modifications

## Installation

```bash
pip install github-api-sdk
```

## Usage

```python
from github_api_sdk import GitHubAPI

gh = GitHubAPI(api_key=...)

issues = gh.repos.issues.list(
    owner="foo",
    repo="bar",
    creator="kenny",
    assignee="spenny",
    direction="desc",
    labels="bug,ui,@high",
    mentioned="bobby",
    milestone=123,
    page=1,
    per_page=100,
    since="2025-04-23T00:00:00Z",
    sort="created",
    state="open",
)

for issue in issues:
    print(issue.number, issue.title)

```
