from __future__ import annotations
import re, requests

from requests_toolbelt import sessions
from typing import Any, Optional

REST_EXPRESSION = re.compile(
    r"(?P<method>GET|OPTIONS|HEAD|PUT|PATCH|POST|DELETE) (?P<url>.+)"
)
URL_REPLACEMENT = re.compile(r"{(?P<var_name>[a-z_]+)}")


class Requester:
    """Requester: a wrapper around requests to make it easy to copy/paste requests from GitHub's API documentation.

    GitHub documents their API calls like:
        GET /repos/{owner}/{repo}
        PATCH /repos/{owner}/{repo}
        PUT /repos/{owner}/{repo}/rulesets/{ruleset_id}

    So with Requester you can pass one of those 'METHOD /url/{variable}' combos into the rest method and have it turned into an input to the requests library.
    """

    def __init__(self, base_url: Optional[str] = None, **kwargs: Any) -> None:
        self.default_replacements = kwargs
        self.session: sessions.BaseUrlSession | requests.sessions.Session

        if base_url:
            self.session = sessions.BaseUrlSession(base_url=base_url)
        else:
            self.session = requests.sessions.Session()

    def rest(
        self, method_and_url: str, body: Optional[Any] = None, **kwargs: Any
    ) -> requests.Response:
        parts = REST_EXPRESSION.match(method_and_url)
        if not parts:
            raise Exception(f"Invalid REST expression: {method_and_url}")

        method = parts.group("method")
        url = parts.group("url")
        for replacement in URL_REPLACEMENT.finditer(url):
            var_name = replacement.group("var_name")
            val = kwargs.pop(var_name, None) or self.default_replacements.get(var_name)
            if val is None:
                continue

            url = url.replace(replacement.group(0), val)

        resp: requests.Response = self.session.request(
            method, url, data=body, params=kwargs
        )

        return resp
