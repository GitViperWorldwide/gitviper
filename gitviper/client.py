from gitviper.base import GithubBase
from gitviper.constants import Version
from result import Result
from typing import List, Optional

from gitviper.schema.organization import Organization
from gitviper.schema.repository import Repository
from gitviper.schema.repository_create import RepositoryCreate
from gitviper.schema.repository_update import RepositoryUpdate
from gitviper.schema.team import Team
from gitviper.schema.team_update import TeamUpdate


class GithubClient(GithubBase):
    def __init__(
        self,
        pat: Optional[str] = None,
        app_id: Optional[str] = None,
        app_pk: Optional[str] = None,
        installation_id: Optional[int] = None,
        default_org: Optional[str] = None,
        base_url: str = "https://api.github.com/",
        api_version: str = Version.v2022_11_28.value,
    ) -> None:
        super().__init__(
            pat=pat,
            app_id=app_id,
            app_pk=app_pk,
            installation_id=installation_id,
            default_org=default_org,
            base_url=base_url,
            api_version=api_version,
        )

    def get_organization(self, org: Optional[str] = None) -> Result[Organization, str]:
        return self.get("/orgs/{org}", Organization, org=org)

    def get_repository(
        self, repo: str, owner: Optional[str] = None
    ) -> Result[Repository, str]:
        return self.get("/repos/{owner}/{repo}", Repository, repo=repo, owner=owner)

    def update_repository(
        self, repo: str, data: RepositoryUpdate, owner: Optional[str] = None
    ) -> Result[Repository, str]:
        return self.send(
            "PATCH /repos/{owner}/{repo}", data, Repository, repo=repo, owner=owner
        )

    def delete_repository(
        self, repo: str, owner: Optional[str] = None
    ) -> Result[None, str]:
        return self.delete("/repos/{owner}/{repo}", repo=repo, owner=owner)

    def list_org_repositories(
        self, org: Optional[str] = None
    ) -> Result[List[Repository], str]:
        return self.paginate("/orgs/{org}/repos", Repository, org=org)

    def create_org_repository(
        self, data: RepositoryCreate, org: Optional[str] = None
    ) -> Result[Repository, str]:
        return self.send("POST /orgs/{org}/repos", data, Repository, org=org)

    def list_org_teams(self, org: Optional[str] = None) -> Result[List[Team], str]:
        return self.paginate("/orgs/{org}/teams", Team, org=org)

    def get_org_team(
        self, team_slug: str, org: Optional[str] = None
    ) -> Result[Team, str]:
        return self.get(
            "/orgs/{org}/teams/{team_slug}", Team, org=org, team_slug=team_slug
        )

    def update_org_team(
        self, team_slug: str, data: TeamUpdate, org: Optional[str] = None
    ) -> Result[Team, str]:
        return self.send(
            "PATCH /orgs/{org}/teams/{team_slug}",
            data,
            Team,
            org=org,
            team_slug=team_slug,
        )

    def delete_org_team(
        self, team_slug: str, org: Optional[str] = None
    ) -> Result[None, str]:
        return self.delete(
            "/orgs/{org}/teams/{team_slug}", org=org, team_slug=team_slug
        )
