"""aioimmich exceptions."""

from __future__ import annotations


class ImmichMissingSetup(Exception):
    """The Immich class had not yet been set up."""

    def __init__(self):
        """Initialize missing setup error."""
        super().__init__(
            "The Immich class had not yet been set up; please run async_setup first"
        )


class ImmichError(Exception):
    """Base class for immich errors."""

    def __init__(self, result: dict):
        """Initialize an immich error."""
        message = result["message"]
        correlation_id = result["correlationId"]
        if "error" in result:
            # immich v2 path
            error = result["error"]
            code = result["statusCode"]
            super().__init__(
                f"{message} (error: '{error}' code: '{code}' correlation_id: '{correlation_id}')"
            )
        elif "errors" in result:
            # immich v3 validation error path
            msg = f"{message} (correlation_id: '{correlation_id}') -"
            for err in result["errors"]:
                msg += f" {err['message']} in path {err['path']}"
            super().__init__(msg)
        else:
            # immich v3 common error path
            super().__init__(f"{message} (correlation_id: '{correlation_id}')")


class ImmichUnauthorizedError(ImmichError):
    """Unauthorized error."""


class ImmichForbiddenError(ImmichError):
    """Forbidden error."""


class ImmichNotFoundError(ImmichError):
    """Not found error."""
