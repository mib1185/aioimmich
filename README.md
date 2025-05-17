[![Test](https://github.com/mib1185/aioimmich/actions/workflows/test.yml/badge.svg)](https://github.com/mib1185/aioimmich/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/mib1185/aioimmich/branch/main/graph/badge.svg?token=QRC1NSIONL)](https://codecov.io/gh/mib1185/aioimmich)
[![Library version](https://img.shields.io/pypi/v/aioimmich.svg)](https://pypi.org/project/aioimmich)
[![Supported versions](https://img.shields.io/pypi/pyversions/aioimmich.svg)](https://pypi.org/project/aioimmich)
[![Formated with Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# aioimmich
Asynchronous library to fetch albums and assests from [immich](https://immich.app/). The main purpose of this library is the integration of an immich instance into [Home Assistant](https://www.home-assistant.io/).

:warning: **this is in early development state** :warning:

breaking changes may occure at every time.

## Requirements

- Python >= 3.9
- aiohttp

## Installation

```bash
pip install aioimmich
```

## Examples

### Get all albums

```python
import asyncio
import aiohttp
from aioimmich import Immich


async def main():
    async with aiohttp.ClientSession() as session:
        immich = Immich(session, "<API-KEY>", "<IMMICH-IP>")

        for album in await immich.albums.async_get_all_albums():
            print(f"Album: {album.name} contains {album.asset_count} assets")


if __name__ == "__main__":
    asyncio.run(main())
```

### Download an asset

```python
import asyncio
import aiohttp
from aioimmich import Immich


async def main():
    async with aiohttp.ClientSession() as session:
        immich = Immich(session, "<API-KEY>", "<IMMICH-IP>")

        asset_bytes = await immich.assets.async_view_asset("<ASSET-ID>", size="fullsize")
        with open(f"my_nice_picture.jpg", "wb") as fh:
            fh.write(asset_bytes)


if __name__ == "__main__":
    asyncio.run(main())
```

### Get server info

```python
import asyncio
import aiohttp
from aioimmich import Immich


async def main():
    async with aiohttp.ClientSession() as session:
        immich = Immich(session, "<API-KEY>", "<IMMICH-IP>")

        about_info = await api.server.async_get_about_info()
        print(f"Version:       {about_info.version}")
        print(f"Is licensed:   {about_info.licensed}")

        storage_info = await api.server.async_get_storage_info()
        print(f"Disk Available:       {storage_info.disk_available}")
        print(f"Disk Available (raw): {storage_info.disk_available_raw} bytes")
        print(f"Disk Size:            {storage_info.disk_size}")
        print(f"Disk Size (raw):      {storage_info.disk_size_raw} bytes")
        print(f"Disk Usage:           {storage_info.disk_usage_percentage}%")
        print(f"Disk Use:             {storage_info.disk_use}")
        print(f"Disk Use (raw):       {storage_info.disk_use_raw} bytes")


if __name__ == "__main__":
    asyncio.run(main())
```
