
from packaging.version import (
    Version,
)
import typing as t

class InvalidInput(SystemExit):
    """Invalid input from user"""


class InvalidIfClause(SystemExit):
    """Invalid if clause in manifest file"""


def to_version(s: t.Any) -> Version:
    if isinstance(s, Version):
        return s

    try:
        return Version(str(s))
    except ValueError:
        raise InvalidInput(f'Invalid version: {s}')
