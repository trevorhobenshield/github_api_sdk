# GitHub API

Fluent GitHub API generated using [Stainless](https://github.com/stainless-api) with modifications

> [!note]
> https://github.blog/changelog/2025-03-06-github-issues-projects-api-support-for-issues-advanced-search-and-more/

## Installation

```bash
pip install github-api-sdk
```

## Usage


```python
from github_api_sdk import GitHubAPI

gh = GitHubAPI(api_key=...)

# list issues
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




# search issues
owner,repo = 'foo','bar'
query = 'baz'
issues = gh.search.issues.search(q=f'{query} in:title repo:{owner}/{repo} state:open')

for issue in issues.items:
    print(issue.number)
```
