from result import Result
from typing import List, Optional

from gitviper.schema.team import Team, TeamUpdate


class TeamMixins:
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

    def list_repository_teams(
        self, repo: str, owner: Optional[str] = None
    ) -> Result[List[Team], str]:
        return self.paginate(
            "/repos/{owner}/{repo}/teams", Team, owner=owner, repo=repo
        )
