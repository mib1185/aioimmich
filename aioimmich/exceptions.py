"""aioimmich exceptions."""

from __future__ import annotations


class ImmichError(Exception):
    """Base class for immich errors."""

    def __init__(self, result: dict):
        """Initialize JSON RPC errors."""
        message = result["message"]
        error = result["error"]
        code = result["statusCode"]
        correlation_id = result["correlationId"]
        super().__init__(
            f"{message} (error: '{error}' code: '{code}' correlation_id: '{correlation_id}')"
        )


class ImmichUnauthorizedError(ImmichError):
    """Unauthorized error."""


class ImmichForbiddenError(ImmichError):
    """Forbidden error."""


class ImmichNotFoundError(ImmichError):
    """Not found error."""
