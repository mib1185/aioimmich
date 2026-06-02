"""aioimmich memories api."""

from __future__ import annotations

from datetime import datetime

from ..api import ImmichSubApi
from .models import ImmichMemory


class ImmichMemories(ImmichSubApi):
    """Immich memories api."""

    async def async_get_all_memories(
        self, for_date: datetime | None = None
    ) -> list[ImmichMemory]:
        """Get all memories.

        Args:
            for_date: Optional `datetime` to filter memories.

        Returns:
            all memories as list of `ImmichMemory`
        """
        params = {}
        if for_date is not None:
            params["for"] = for_date.isoformat()

        result = await self.api.async_do_request("memories", params=params)
        assert isinstance(result, list)
        return [ImmichMemory.from_dict(tag) for tag in result]

    async def async_get_memory(self, memory_id: str) -> ImmichMemory:
        """Get a specific memory by ID.

        Args:
            memory_id: The ID of the memory to retrieve.

        Returns:
            a memory as `ImmichMemory`
        """
        result = await self.api.async_do_request(f"memories/{memory_id}")
        assert isinstance(result, dict)
        return ImmichMemory.from_dict(result)
