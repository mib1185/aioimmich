"""aioimmich exceptions."""

from enum import Enum


class StrEnum(str, Enum):
    """
    Enum where members are also (and must be) strings.

    This is a copy of the StrEnum which is introduced in python 3.11
    """

    def __new__(cls, *values):
        """Values must already be of type `str`."""
        if len(values) > 3:
            raise TypeError(f"too many arguments for str(): {values}")
        if len(values) == 1:
            # it must be a string
            if not isinstance(values[0], str):
                raise TypeError(f"{values[0]} is not a string")
        if len(values) >= 2:
            # check that encoding argument is a string
            if not isinstance(values[1], str):
                raise TypeError(f"encoding must be a string, not {values[1]}")
        if len(values) == 3:
            # check that errors argument is a string
            if not isinstance(values[2], str):
                raise TypeError(f"errors must be a string, not {values[2]}")
        value = str(*values)
        member = str.__new__(cls, value)
        member._value_ = value
        return member

    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        """Return the lower-cased version of the member name."""
        return name.lower()
