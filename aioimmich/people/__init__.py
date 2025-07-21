"""aioimmich people api."""

from ..api import ImmichSubApi
from .models import ImmichPerson


class ImmichPeople(ImmichSubApi):
    """Immich tags api."""

    async def async_get_all_people(
        self, with_unnamed: bool = False, page_size: int = 3, max_pages: int = 1
    ) -> list[ImmichPerson]:
        """Get all people.

        Args:
            page_size (int):  assets per page
            max_pages (int):  maximun number of pages to return

        Returns:
            all people as list of `ImmichPerson`
        """
        results: list[ImmichPerson] = []
        for page in range(max_pages):
            result = await self.api.async_do_request(
                "people", params={"size": page_size, "page": page + 1}
            )
            assert isinstance(result, dict)
            people = result["people"]
            results.extend(
                ImmichPerson.from_dict(person)
                for person in people
                if person["name"] or with_unnamed
            )
            if not result.get("hasNextPage"):
                break

        return results

    async def async_get_person_thumbnail(self, person_id: str) -> bytes:
        """Download thumbnail for a person.

        Args:
            person_id (str): id of the person to fetch the thumbnail for

        Returns:
            persons thumbnail as `bytes`
        """
        result = await self.api.async_do_request(
            f"people/{person_id}/thumbnail", application="octet-stream"
        )
        assert isinstance(result, bytes)
        return result
