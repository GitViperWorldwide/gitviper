class AuthenticationException(Exception):
    """Cause by an issue during authentication"""


class InvalidRestExpressionException(Exception):
    """REST expression doesn't match 'VERB /url/here' pattern"""


class MissingReplacementException(Exception):
    """A variable in the url was not supplied a replacement value"""


class InvalidPaginatedData(Exception):
    """The received data was not in the expected list format"""
