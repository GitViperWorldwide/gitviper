from __future__ import annotations
import re, requests

from dataclasses import dataclass
from enum import StrEnum
from gitviper.exceptions import (
    InvalidRestExpressionException,
    MissingReplacementException,
)
from requests_toolbelt import sessions
from typing import Any, Optional

URL_REPLACEMENT = re.compile(r"{(?P<var_name>[a-z_]+)}")


class HTTPMethod(StrEnum):
    GET = "GET"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    PUT = "PUT"
    PATCH = "PATCH"
    POST = "POST"
    DELETE = "DELETE"


@dataclass
class MethodAndURL:
    method: HTTPMethod
    url: str

    @classmethod
    def from_string(cls, input: str) -> MethodAndURL:
        try:
            method, url = input.split(" ", 1)
            return cls(HTTPMethod(method), url)
        except:
            raise InvalidRestExpressionException()


class Requester:
    """Requester: a wrapper around requests to make it easy to copy/paste requests from GitHub's API documentation.

    GitHub documents their API calls like:
        GET /repos/{owner}/{repo}
        PATCH /repos/{owner}/{repo}
        PUT /repos/{owner}/{repo}/rulesets/{ruleset_id}

    So with Requester you can pass one of those 'METHOD /url/{variable}' combos into the rest method and have it turned into an input to the requests library.
    """

    def __init__(self, base_url: Optional[str] = None, **kwargs: Any) -> None:
        """Initializes a Requester session

        Args:
            base_url: an optional base URL to prepend to partial URLs supplied to the rest method

            kwargs: key/value pairs that will be the defaults for variable replacements in the rest method's supplied URL.
        """

        self.default_replacements = kwargs
        self.session: sessions.BaseUrlSession | requests.sessions.Session

        if base_url:
            self.session = sessions.BaseUrlSession(base_url=base_url)
        else:
            self.session = requests.sessions.Session()

    def rest(
        self, method_and_url: str, body: Optional[Any] = None, **kwargs: Any
    ) -> requests.Response:
        """Wrapper around requests.Request

        Args:
            method_and_url: a HTTP method (GET|OPTIONS|HEAD|PUT|PATCH|POST|DELETE) followed by a url with optional variables in {variable_name} format.
            body: optional data to send as the body of the request.
            kwargs: any argument with a name matching a variable in the URL will replace that variable, all other arguments are sent as query parameters.

        Returns:
            A requests.Response object

        Raises:
            InvalidRestExpressionException: the method_and_url do not match the expected pattern

            MissingReplacementException: a variable in the URL was not supplied a kwarg value
        """

        parts = MethodAndURL.from_string(method_and_url)

        url = parts.url
        for replacement in URL_REPLACEMENT.finditer(url):
            var_name = replacement.group("var_name")
            val = kwargs.pop(var_name, None) or self.default_replacements.get(var_name)
            if val is None:
                raise MissingReplacementException(f"{var_name} not included in kwargs")

            url = url.replace(replacement.group(0), str(val))

        resp: requests.Response = self.session.request(
            f"{parts.method}", url, data=body, params=kwargs
        )

        return resp
