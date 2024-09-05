from result import Result
from typing import List, Optional

from gitviper.schema.repository import Repository, RepositoryCreate, RepositoryUpdate
from gitviper.schema.tag import Tag
from gitviper.schema.topic import Topic, Topics


class RepositoryMixins:
    def get_repository(self, repo: str, owner: Optional[str] = None) -> Result[Repository, str]:
        return self.get("/repos/{owner}/{repo}", Repository, repo=repo, owner=owner)

    def update_repository(self, repo: str, data: RepositoryUpdate, owner: Optional[str] = None) -> Result[Repository, str]:
        return self.send("PATCH /repos/{owner}/{repo}", data, Repository, repo=repo, owner=owner)

    def delete_repository(self, repo: str, owner: Optional[str] = None) -> Result[None, str]:
        return self.delete("/repos/{owner}/{repo}", repo=repo, owner=owner)

    def list_org_repositories(self, org: Optional[str] = None) -> Result[List[Repository], str]:
        return self.paginate("/orgs/{org}/repos", Repository, org=org)

    def create_org_repository(self, data: RepositoryCreate, org: Optional[str] = None) -> Result[Repository, str]:
        return self.send("POST /orgs/{org}/repos", data, Repository, org=org)

    def list_user_repositories(self, username: str) -> Result[List[Repository], str]:
        return self.paginate("/users/{username}/repos", Repository, username=username)

    def list_repository_tags(self, repo: str, owner: Optional[str] = None) -> Result[List[Tag], str]:
        return self.paginate("/repos/{owner}/{repo}/tags", Tag, owner=owner, repo=repo)

    def list_repository_topics(self, repo: str, owner: Optional[str] = None) -> Result[List[Topic], str]:
        return self.paginate(
            "/repos/{owner}/{repo}/topics",
            Topic,
            sub_property="names",
            owner=owner,
            repo=repo,
        )

    def replace_repository_topics(self, repo: str, data: Topics, owner: Optional[str] = None) -> Result[Topics, str]:
        return self.send("PUT /repos/{owner}/{repo}/topics", data, Topics, repo=repo, owner=owner)
