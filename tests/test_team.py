import responses

from gitviper.schema.team import Permission, TeamUpdate

from responses import matchers
from tests.helpers import BASE_URL, github_client

team_response = """{
  "id": 1,
  "node_id": "MDQ6VGVhbTE=",
  "url": "https://api.github.com/teams/1",
  "html_url": "https://github.com/orgs/github/teams/justice-league",
  "name": "Justice League",
  "slug": "justice-league",
  "description": "A great team.",
  "privacy": "closed",
  "notification_setting": "notifications_enabled",
  "permission": "admin",
  "members_url": "https://api.github.com/teams/1/members{/member}",
  "repositories_url": "https://api.github.com/teams/1/repos",
  "parent": null,
  "members_count": 3,
  "repos_count": 10,
  "created_at": "2017-07-14T16:53:42Z",
  "updated_at": "2017-08-17T12:37:15Z",
  "organization": {
    "login": "github",
    "id": 1,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjE=",
    "url": "https://api.github.com/orgs/github",
    "repos_url": "https://api.github.com/orgs/github/repos",
    "events_url": "https://api.github.com/orgs/github/events",
    "hooks_url": "https://api.github.com/orgs/github/hooks",
    "issues_url": "https://api.github.com/orgs/github/issues",
    "members_url": "https://api.github.com/orgs/github/members{/member}",
    "public_members_url": "https://api.github.com/orgs/github/public_members{/member}",
    "avatar_url": "https://github.com/images/error/octocat_happy.gif",
    "description": "A great organization",
    "name": "github",
    "company": "GitHub",
    "blog": "https://github.com/blog",
    "location": "San Francisco",
    "email": "octocat@github.com",
    "is_verified": true,
    "has_organization_projects": true,
    "has_repository_projects": true,
    "public_repos": 2,
    "public_gists": 1,
    "followers": 20,
    "following": 0,
    "html_url": "https://github.com/octocat",
    "created_at": "2008-01-14T04:33:35Z",
    "updated_at": "2017-08-17T12:37:15Z",
    "type": "Organization"
  }
}"""


@responses.activate
def test_get_team():
    gh = github_client()

    responses.get(f"{BASE_URL}/orgs/an-org/teams/a-team", body=team_response)

    result = gh.get_org_team("a-team", org="an-org")

    assert result.err() is None
    team = result.ok()
    assert team.name == "Justice League"
    assert team.created_at.year == 2017


@responses.activate
def test_list_teams():
    gh = github_client()

    responses.get(f"{BASE_URL}/orgs/an-org/teams", body=f"[{team_response}]")

    result = gh.list_org_teams(org="an-org")

    assert result.err() is None
    assert len(result.ok()) == 1
    team = result.ok()[0]
    assert team.name == "Justice League"
    assert team.created_at.year == 2017


@responses.activate
def test_update_team():
    gh = github_client()

    responses.patch(
        f"{BASE_URL}/orgs/an-org/teams/a-team",
        match=[matchers.json_params_matcher({"description": "a new description", "permission": "admin"})],
        body=team_response,
    )

    result = gh.update_org_team(
        "a-team",
        TeamUpdate(description="a new description", permission=Permission.admin),
        org="an-org",
    )

    assert result.err() is None
    team = result.ok()
    assert team.name == "Justice League"


@responses.activate
def test_delete_team():
    gh = github_client()

    responses.delete(f"{BASE_URL}/orgs/an-org/teams/a-team", status=204)

    result = gh.delete_org_team("a-team", org="an-org")

    assert result.err() is None


@responses.activate
def test_list_repo_teams():
    gh = github_client()

    responses.get(f"{BASE_URL}/repos/a-user/a-repo/teams", body=f"[{team_response}]")

    result = gh.list_repository_teams("a-repo", owner="a-user")

    assert result.err() is None
    assert len(result.ok()) == 1
    team = result.ok()[0]
    assert team.name == "Justice League"
    assert team.created_at.year == 2017
