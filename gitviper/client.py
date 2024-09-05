from __future__ import annotations

import jwt, re, time

from dataclasses import dataclass
from datetime import datetime, timezone
from requests import Timeout
from result import Err, Ok, Result
from traceback import format_exc
from typing import Any, List, Optional, TYPE_CHECKING
from urllib.parse import urlparse, parse_qs, ParseResult

from gitviper.constants import Version
from gitviper.exceptions import AuthenticationException, InvalidPaginatedData
from gitviper.requester import Requester
from gitviper.schema.installation_token import InstallationToken

from gitviper.api_mixins.org import OrgMixins
from gitviper.api_mixins.repo import RepositoryMixins
from gitviper.api_mixins.team import TeamMixins

if TYPE_CHECKING:  # pragma: no cover
    import requests, requests.adapters
    from pydantic import BaseModel


LINK_HEADER_EXPRESSION = re.compile(r"\<(?P<url>.+?)\>; rel=\"(?P<rel>[a-z_]+)\"")


@dataclass
class Rate:
    remaining: int
    reset: datetime

    @classmethod
    def from_headers(cls, headers: requests.adapters.CaseInsensitiveDict) -> Rate:
        remaining: int
        try:
            remaining = int(headers.get("x-ratelimit-remaining", "1"))
        except:
            remaining = 1

        reset: datetime
        try:
            reset = datetime.fromtimestamp(float(headers.get("x-ratelimit-reset", "0")))
        except:
            reset = datetime.now(timezone.utc)

        return cls(remaining, reset)


class GithubClient(Requester, RepositoryMixins, OrgMixins, TeamMixins):
    def __init__(
        self,
        pat: Optional[str] = None,
        app_id: Optional[str] = None,
        app_pk: Optional[str] = None,
        app_pk_algorithm: Optional[str] = "RS256",
        installation_id: Optional[int] = None,
        default_org: Optional[str] = None,
        base_url: str = "https://api.github.com/",
        api_version: str = Version.v2022_11_28.value,
    ) -> None:
        self.pat = pat
        self.app_id = app_id
        self.app_pk = app_pk
        self.app_pk_algorithm = app_pk_algorithm
        self.installation_id = installation_id
        self.api_version = api_version
        self.token_expiry: Optional[datetime] = None

        self.rate: Optional[Rate] = None

        super().__init__(base_url, **{"owner": default_org, "org": default_org})

        self.session.headers.update(
            {
                "X-GitHub-Api-Version": api_version,
                "Accept": "application/vnd.github+json",
            }
        )

        self.authenticate()
        self.get_rate_limit()

    def generate_jwt(self) -> str:
        now = int(time.time())
        return str(
            jwt.encode(
                {"iat": now, "exp": now + 600, "iss": int(self.app_id)},
                self.app_pk.replace("\\n", "\n"),
                algorithm=self.app_pk_algorithm,
            )
        )

    def authenticate(self) -> None:
        if self.pat:
            self.session.headers.update({"Authorization": f"Bearer {self.pat}"})
        elif self.app_id and self.app_pk and self.installation_id:
            token_resp = self.session.post(
                f"/app/installations/{self.installation_id}/access_tokens",
                headers={"Authorization": f"Bearer {self.generate_jwt()}"},
            )

            if token_resp.ok:
                data = InstallationToken.model_validate(token_resp.json())

                self.token_expiry = datetime.fromisoformat(data.expires_at)
                self.session.headers.update({"Authorization": f"Bearer {data.token}"})
            else:
                raise AuthenticationException(
                    f"Unable to get app installations: {token_resp.text}"
                )
        else:
            raise AuthenticationException(
                "A personal access token or (app id, private key, and installation ID) must be specified"
            )

    def _check_token_expiry(self) -> None:
        if self.token_expiry is None:
            return
        if datetime.now(timezone.utc) > self.token_expiry:
            self.authenticate()

    def _update_rate_limit(self, response: requests.Response) -> None:
        self.rate = Rate.from_headers(response.headers)

    def _check_rate_limit(self) -> None:
        if not self.rate:
            return
        if self.rate.remaining == 0 and datetime.now(timezone.utc) < self.rate.reset:
            # TODO wait
            pass

    def get[
        T: BaseModel
    ](self, url: str, data_class: T, **kwargs: Any) -> Result[T, str]:
        self._check_rate_limit()
        self._check_token_expiry()

        try:
            resp = self.rest(f"GET {url}", **kwargs)
            self._update_rate_limit(resp)
            if not resp.ok:
                return Err(f"{resp.status_code} received from '{url}': {resp.text}")
        except Timeout:
            return self.get(url, data_class, **kwargs)  # retry
        except Exception:
            return Err(f"Unhandled exception calling 'GET {url}': {format_exc()}")

        try:
            model = data_class.model_validate(resp.json())
            return Ok(model)
        except Exception:
            return Err(
                f"Unhandled exception parsing response data: {format_exc()}\n\nResponse: {resp.text}"
            )

    def paginate[
        T: BaseModel
    ](
        self, url: str, data_class: T, sub_property: Optional[str] = None, **kwargs: Any
    ) -> Result[List[T], str]:
        kwargs.setdefault("per_page", 100)
        kwargs.setdefault("page", 1)

        data = []
        link: Optional[str] = f"GET {url}"
        while link:
            self._check_rate_limit()
            self._check_token_expiry()
            resp = self.rest(link, **kwargs)
            self._update_rate_limit(resp)

            if not resp.ok:
                return Err(f"{resp.status_code} returned from {link}: {resp.text}")

            try:
                if sub_property:
                    data.extend(resp.json().get(sub_property))
                else:
                    data.extend(resp.json())
            except Exception as e:
                raise InvalidPaginatedData(e)

            parsed_link = self._parse_link_header(resp.headers)
            if parsed_link is None:
                link = None
                continue
            link = f"GET {parsed_link.path}"
            query = parse_qs(parsed_link.query)
            pages = query.get("page", [])
            if len(pages) > 0:
                kwargs["page"] = pages[0]
            else:
                link = None

        parsed_data: List[T] = []
        for item in data:
            try:
                parsed = data_class.model_validate(item)
                parsed_data.append(parsed)
            except Exception as e:
                return Err(f"Error parsing data: {format_exc()}\n\nData: {item}")

        return Ok(parsed_data)

    def send[
        T: BaseModel
    ](
        self,
        method_and_url: str,
        data: BaseModel,
        response_data_class: T,
        **kwargs: Any,
    ) -> Result[T, str]:
        self._check_rate_limit()
        self._check_token_expiry()

        try:
            resp = self.rest(
                method_and_url, body=data.model_dump_json(exclude_none=True), **kwargs
            )
            self._update_rate_limit(resp)
            if not resp.ok:
                return Err(
                    f"{resp.status_code} received from '{method_and_url}': {resp.text}"
                )
        except Timeout:
            return self.send(
                method_and_url, data, response_data_class, **kwargs
            )  # retry
        except Exception:
            return Err(
                f"Unhandled exception calling '{method_and_url}': {format_exc()}"
            )

        try:
            return Ok(response_data_class.model_validate(resp.json()))
        except Exception:
            return Err(
                f"Unhandled exception parsing response data: {format_exc()}\n\nResponse: {resp.text}"
            )

    def delete(self, url: str, **kwargs) -> Result[None, str]:
        self._check_rate_limit()
        self._check_token_expiry()
        resp = self.rest(f"DELETE {url}", **kwargs)
        self._update_rate_limit(resp)

        if resp.status_code == 204:
            return Ok(None)

        return Err(f"{resp.status_code} returned from {url}: {resp.text}")

    def get_rate_limit(self) -> None:
        resp = self.rest("GET /rate_limit")
        if resp.ok:
            self._update_rate_limit(resp)

    def _parse_link_header(
        self,
        headers: requests.adapters.CaseInsensitiveDict,  # type: ignore
        rel: str = "next",
    ) -> Optional[ParseResult]:
        links: Optional[str] = headers.get("link")
        if links is None:
            return None

        for link in LINK_HEADER_EXPRESSION.finditer(links):
            if link.group("rel") == rel:
                l = link.group("url")
                if l is None:
                    return None
                return urlparse(l)

        return None
