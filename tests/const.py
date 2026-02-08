"""Constants for aioimmich tests."""

import json

from aiohttp import ClientError

MOCK_IMMICH_HOST = "localhost"
MOCK_IMMICH_API_KEY = "abcdef1234567890"

MOCK_DATA_ALBUM_1: dict = {
    "albumName": "Album 1",
    "description": "My first great album",
    "albumThumbnailAssetId": "0d03a7ad-ddc7-45a6-adee-68d322a6d2f5",
    "createdAt": "2025-05-11T10:13:22.799Z",
    "updatedAt": "2025-05-17T11:26:03.696Z",
    "id": "721e1a4b-aa12-441e-8d3b-5ac7ab283bb6",
    "ownerId": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
    "owner": {
        "id": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
        "email": "admin@myhost.local",
        "name": "admin",
        "profileImagePath": "",
        "avatarColor": "pink",
        "profileChangedAt": "2025-05-11T10:07:46.86688+00:00",
    },
    "albumUsers": [],
    "shared": False,
    "hasSharedLink": False,
    "startDate": "2022-11-15T00:00:00.000Z",
    "endDate": "2025-05-13T00:00:00.000Z",
    "assets": [],
    "assetCount": 4,
    "isActivityEnabled": True,
    "order": "desc",
    "lastModifiedAssetTimestamp": "2025-05-14T19:15:27.455Z",
}

MOCK_DATA_ALBUM_1_ASSETS: list[dict] = [
    {
        "id": "2e94c203-50aa-4ad2-8e29-56dd74e0eff4",
        "deviceAssetId": "web-20230131_182037.jpg-1675185639000",
        "ownerId": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
        "deviceId": "WEB",
        "libraryId": None,
        "type": "IMAGE",
        "originalPath": "upload/upload/e7ef5713-9dab-4bd4-b899-715b0ca4379e/b4/b8/b4b8ef00-8a6d-4056-91ff-7f86dc66e427.jpg",
        "originalFileName": "20230131_182037.jpg",
        "originalMimeType": "image/jpeg",
        "thumbhash": "1igGFALX8mVGdHc5aChJf5nxNg==",
        "fileCreatedAt": "2023-01-31T17:20:37.085+00:00",
        "fileModifiedAt": "2023-01-31T17:20:39+00:00",
        "localDateTime": "2023-01-31T18:20:37.085+00:00",
        "updatedAt": "2025-05-11T10:13:49.590401+00:00",
        "isFavorite": False,
        "isArchived": False,
        "isTrashed": False,
        "duration": "0:00:00.00000",
        "exifInfo": {},
        "livePhotoVideoId": None,
        "people": [],
        "checksum": "HJm7TVOP80S+eiYZnAhWyRaB/Yc=",
        "isOffline": False,
        "hasMetadata": True,
        "duplicateId": None,
        "resized": True,
    },
    {
        "id": "de104b75-6c7f-46a2-83ce-12a5b1c3a3b4",
        "deviceAssetId": "web-20221222_205943.jpg-1671739185000",
        "ownerId": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
        "deviceId": "WEB",
        "libraryId": None,
        "type": "IMAGE",
        "originalPath": "upload/upload/e7ef5713-9dab-4bd4-b899-715b0ca4379e/43/ab/43abc8a2-3f81-4afc-95ea-c784cf869e4c.jpg",
        "originalFileName": "20221222_205943.jpg",
        "originalMimeType": "image/jpeg",
        "thumbhash": "kWkGDAR9CGRpWO11VpJ2cGtVCQ==",
        "fileCreatedAt": "2022-12-22T19:59:43.095+00:00",
        "fileModifiedAt": "2022-12-22T19:59:45+00:00",
        "localDateTime": "2022-12-22T20:59:43.095+00:00",
        "updatedAt": "2025-05-11T10:13:49.590877+00:00",
        "isFavorite": False,
        "isArchived": False,
        "isTrashed": False,
        "duration": "0:00:00.00000",
        "exifInfo": {},
        "livePhotoVideoId": None,
        "people": [],
        "checksum": "aNCzp51jAuT3rXMv1icKLGMTC6M=",
        "isOffline": False,
        "hasMetadata": True,
        "duplicateId": None,
        "resized": True,
    },
    {
        "id": "7d9ecb29-b12a-498d-adf9-c6ac09c761d3",
        "deviceAssetId": "web-20221222_185242.jpg-1671731574000",
        "ownerId": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
        "deviceId": "WEB",
        "libraryId": None,
        "type": "IMAGE",
        "originalPath": "upload/upload/e7ef5713-9dab-4bd4-b899-715b0ca4379e/4f/a7/4fa7280f-16e6-4eb8-938a-89770266a20d.jpg",
        "originalFileName": "20221222_185242.jpg",
        "originalMimeType": "image/jpeg",
        "thumbhash": "FUoGNAKHV4f4ZoLXZ1d2cl9H9w==",
        "fileCreatedAt": "2022-12-22T17:52:44.097+00:00",
        "fileModifiedAt": "2022-12-22T17:52:54+00:00",
        "localDateTime": "2022-12-22T18:52:44.097+00:00",
        "updatedAt": "2025-05-11T10:13:49.590479+00:00",
        "isFavorite": False,
        "isArchived": False,
        "isTrashed": False,
        "duration": "0:00:00.00000",
        "exifInfo": {},
        "livePhotoVideoId": None,
        "people": [],
        "checksum": "8fDGDOnOCVkJK8KiNu1bSmytEQ4=",
        "isOffline": False,
        "hasMetadata": True,
        "duplicateId": None,
        "resized": True,
    },
    {
        "id": "1ed37a88-c720-49b9-bc3d-0e78aab3099a",
        "deviceAssetId": "web-20221115_185642.jpg-1668535006000",
        "ownerId": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
        "deviceId": "WEB",
        "libraryId": None,
        "type": "IMAGE",
        "originalPath": "upload/upload/e7ef5713-9dab-4bd4-b899-715b0ca4379e/7c/86/7c8643f0-f91e-4926-8e6a-8e8c4403e4d0.jpg",
        "originalFileName": "20221115_185642.jpg",
        "originalMimeType": "image/jpeg",
        "thumbhash": "UBgODIJvdKmYZmZ2Z3cPlfUjaQ==",
        "fileCreatedAt": "2022-11-15T17:56:42.077+00:00",
        "fileModifiedAt": "2022-11-15T17:56:46+00:00",
        "localDateTime": "2022-11-15T18:56:42.077+00:00",
        "updatedAt": "2025-05-11T10:13:49.766801+00:00",
        "isFavorite": False,
        "isArchived": False,
        "isTrashed": False,
        "duration": "0:00:00.00000",
        "exifInfo": {},
        "livePhotoVideoId": None,
        "people": [],
        "checksum": "RA2WL5H511G+A7f1hV8+jJdfUUQ=",
        "isOffline": False,
        "hasMetadata": True,
        "duplicateId": None,
        "resized": True,
    },
]

MOCK_DATA_ALBUM_2: dict = {
    "albumName": "Album 2",
    "description": "Not so great second album",
    "albumThumbnailAssetId": "6961329c-d8ee-4f09-9d4e-6997ea5b7bf4",
    "createdAt": "2025-05-12T20:48:30.784Z",
    "updatedAt": "2025-05-17T11:34:53.942Z",
    "id": "c4721c25-8669-451f-a6be-3d9d4dc38f5f",
    "ownerId": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
    "owner": {
        "id": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
        "email": "admin@myhost.local",
        "name": "admin",
        "profileImagePath": "",
        "avatarColor": "pink",
        "profileChangedAt": "2025-05-11T10:07:46.86688+00:00",
    },
    "albumUsers": [],
    "shared": False,
    "hasSharedLink": False,
    "startDate": "2017-04-11T00:00:00.000Z",
    "endDate": "2025-05-08T00:00:00.000Z",
    "assets": [],
    "assetCount": 426,
    "isActivityEnabled": True,
    "order": "desc",
    "lastModifiedAssetTimestamp": "2025-05-17T11:34:54.077Z",
}

MOCK_DATA_SHAED_ALBUM: dict = {
    "albumName": "Shared Album",
    "description": "",
    "albumThumbnailAssetId": "1c148516-3a5d-442d-b74d-9714b257b120",
    "createdAt": "2025-05-11T10:54:49.395Z",
    "updatedAt": "2026-02-08T17:34:53.762Z",
    "id": "8cb7ad53-acb0-4844-be8b-9e4323f0d32d",
    "ownerId": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
    "owner": {
        "id": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
        "email": "admin@immich.local",
        "name": "admin",
        "profileImagePath": "",
        "avatarColor": "primary",
        "profileChangedAt": "2025-05-11T10:07:46.866Z",
    },
    "albumUsers": [
        {
            "user": {
                "id": "568fb168-5022-4cf3-ae16-d4b5c50f5894",
                "email": "test@immich.local",
                "name": "TestUser",
                "profileImagePath": "",
                "avatarColor": "purple",
                "profileChangedAt": "2025-05-18T15:40:50.162463+00:00",
            },
            "role": "viewer",
        }
    ],
    "shared": True,
    "hasSharedLink": False,
    "startDate": "2017-06-08T00:00:00.000Z",
    "endDate": "2025-03-21T00:00:00.000Z",
    "assets": [],
    "assetCount": 69,
    "isActivityEnabled": True,
    "order": "desc",
    "lastModifiedAssetTimestamp": "2026-01-28T22:42:19.894Z",
}

MOCK_DATA: dict = {
    "albums": {
        "status": 200,
        "body": json.dumps([MOCK_DATA_ALBUM_1, MOCK_DATA_ALBUM_2]),
    },
    "albums?shared=true": {
        "status": 200,
        "body": json.dumps([MOCK_DATA_SHAED_ALBUM]),
    },
    f"albums/{MOCK_DATA_ALBUM_1['id']}?withoutAssets=true": {
        "status": 200,
        "body": json.dumps(MOCK_DATA_ALBUM_1),
    },
    f"albums/{MOCK_DATA_ALBUM_1['id']}?withoutAssets=false": {
        "status": 200,
        "body": json.dumps({**MOCK_DATA_ALBUM_1, "assets": MOCK_DATA_ALBUM_1_ASSETS}),
    },
    "assets/2e94c203-50aa-4ad2-8e29-56dd74e0eff4/thumbnail?size=thumbnail": {
        "status": 200,
        "body": b"abcdef",
    },
    "assets/2e94c203-50aa-4ad2-8e29-56dd74e0eff4/thumbnail?size=preview": {
        "status": 200,
        "body": b"abcdefabcdef",
    },
    "assets/2e94c203-50aa-4ad2-8e29-56dd74e0eff4/thumbnail?size=fullsize": {
        "status": 200,
        "body": b"abcdefabcdefabcdefabcdef",
    },
    "users/me": {
        "status": 200,
        "body": json.dumps(
            {
                "id": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
                "email": "admin@immich.local",
                "name": "admin",
                "profileImagePath": "",
                "avatarColor": "primary",
                "profileChangedAt": "2025-05-11T10:07:46.866Z",
                "storageLabel": "admin",
                "shouldChangePassword": True,
                "isAdmin": True,
                "createdAt": "2025-05-11T10:07:46.866Z",
                "deletedAt": None,
                "updatedAt": "2025-05-18T00:59:55.547Z",
                "oauthId": "",
                "quotaSizeInBytes": None,
                "quotaUsageInBytes": 119526467534,
                "status": "active",
                "license": None,
            }
        ),
    },
    "server/about": {
        "status": 200,
        "body": json.dumps(
            {
                "version": "v1.132.3",
                "versionUrl": "https://github.com/immich-app/immich/releases/tag/v1.132.3",
                "licensed": False,
                "build": "14709928600",
                "buildUrl": "https://github.com/immich-app/immich/actions/runs/14709928600",
                "buildImage": "v1.132.3",
                "buildImageUrl": "https://github.com/immich-app/immich/pkgs/container/immich-server",
                "repository": "immich-app/immich",
                "repositoryUrl": "https://github.com/immich-app/immich",
                "sourceRef": "v1.132.3",
                "sourceCommit": "02994883fe3f3972323bb6759d0170a4062f5236",
                "sourceUrl": "https://github.com/immich-app/immich/commit/02994883fe3f3972323bb6759d0170a4062f5236",
                "nodejs": "v22.14.0",
                "exiftool": "13.00",
                "ffmpeg": "7.0.2-7",
                "libvips": "8.16.1",
                "imagemagick": "7.1.1-47",
            }
        ),
    },
    "server/storage": {
        "status": 200,
        "body": json.dumps(
            {
                "diskSize": "294.2 GiB",
                "diskUse": "142.9 GiB",
                "diskAvailable": "136.3 GiB",
                "diskSizeRaw": 315926315008,
                "diskUseRaw": 153400406016,
                "diskAvailableRaw": 146403004416,
                "diskUsagePercentage": 48.56,
            }
        ),
    },
    "server/statistics": {
        "status": 200,
        "body": json.dumps(
            {
                "photos": 27038,
                "videos": 1836,
                "usage": 119525451912,
                "usagePhotos": 54291170551,
                "usageVideos": 65234281361,
                "usageByUser": [
                    {
                        "userId": "e7ef5713-9dab-4bd4-b899-715b0ca4379e",
                        "userName": "admin",
                        "photos": 27038,
                        "videos": 1836,
                        "usage": 119525451912,
                        "usagePhotos": 54291170551,
                        "usageVideos": 65234281361,
                        "quotaSizeInBytes": None,
                    }
                ],
            }
        ),
    },
    "server/version-check": {
        "status": 200,
        "body": json.dumps(
            {"checkedAt": "2025-05-30T20:51:00.325Z", "releaseVersion": "v1.134.0"}
        ),
    },
    "tags": {
        "status": 200,
        "body": json.dumps(
            [
                {
                    "id": "14ce3af3-67be-41c6-b77c-b25abddaf546",
                    "name": "My 30th birthday",
                    "value": "My 30th birthday",
                    "createdAt": "2025-05-12T20:01:24.330Z",
                    "updatedAt": "2025-05-12T20:01:24.412Z",
                },
                {
                    "id": "67301cb8-cb73-4e8a-99e9-475cb3f7e7b5",
                    "name": "Halloween",
                    "value": "Halloween",
                    "createdAt": "2025-05-12T20:00:45.220Z",
                    "updatedAt": "2025-05-12T20:00:47.224Z",
                },
                {
                    "id": "69bd487f-dc1e-4420-94c6-656f0515773d",
                    "name": "Holidays",
                    "value": "Holidays",
                    "createdAt": "2025-05-12T20:00:49.967Z",
                    "updatedAt": "2025-05-12T20:00:55.575Z",
                },
            ]
        ),
    },
    "people?page=1&size=3": {
        "status": 200,
        "body": json.dumps(
            {
                "people": [
                    {
                        "id": "6176838a-ac5a-4d1f-9a35-91c591d962d8",
                        "name": "Me",
                        "birthDate": None,
                        "thumbnailPath": "upload/thumbs/e7ef5713-9dab-4bd4-b899-715b0ca4379e/61/76/6176838a-ac5a-4d1f-9a35-91c591d962d8.jpeg",
                        "isHidden": False,
                        "isFavorite": False,
                        "updatedAt": "2025-05-11T11:07:41.651Z",
                    },
                    {
                        "id": "3e66aa4a-a4a8-41a4-86fe-2ae5e490078f",
                        "name": "I",
                        "birthDate": None,
                        "thumbnailPath": "upload/thumbs/e7ef5713-9dab-4bd4-b899-715b0ca4379e/3e/66/3e66aa4a-a4a8-41a4-86fe-2ae5e490078f.jpeg",
                        "isHidden": False,
                        "isFavorite": False,
                        "updatedAt": "2025-05-19T22:10:21.953Z",
                    },
                    {
                        "id": "a3c83297-684a-4576-82dc-b07432e8a18f",
                        "name": "Myself",
                        "birthDate": None,
                        "thumbnailPath": "upload/thumbs/e7ef5713-9dab-4bd4-b899-715b0ca4379e/a3/c8/a3c83297-684a-4576-82dc-b07432e8a18f.jpeg",
                        "isHidden": False,
                        "isFavorite": False,
                        "updatedAt": "2025-05-12T21:07:04.044Z",
                    },
                ],
                "hasNextPage": False,
                "total": 3,
                "hidden": 0,
            }
        ),
    },
    "people?size=1": {
        "status": 200,
        "body": json.dumps(
            {
                "people": [
                    {
                        "id": "6176838a-ac5a-4d1f-9a35-91c591d962d8",
                        "name": "Me",
                        "birthDate": None,
                        "thumbnailPath": "upload/thumbs/e7ef5713-9dab-4bd4-b899-715b0ca4379e/61/76/6176838a-ac5a-4d1f-9a35-91c591d962d8.jpeg",
                        "isHidden": False,
                        "isFavorite": False,
                        "updatedAt": "2025-05-11T11:07:41.651Z",
                    },
                ],
                "hasNextPage": False,
                "total": 3,
                "hidden": 0,
            }
        ),
    },
    "albums/INVALID_ALBUM_ID?withoutAssets=false": {
        "status": 400,
        "body": json.dumps(
            {
                "message": "Not found or no album.read access",
                "error": "Bad Request",
                "statusCode": 400,
                "correlationId": "e0hlizyl",
            }
        ),
    },
    "albums/INVALID_API_KEY?withoutAssets=false": {
        "status": 401,
        "body": json.dumps(
            {
                "message": "Invalid API key",
                "error": "Unauthorized",
                "statusCode": 401,
                "correlationId": "qouswiyh",
            }
        ),
    },
    "albums/FORBIDDEN?withoutAssets=false": {
        "status": 403,
        "body": json.dumps(
            {
                "message": "Forbidden",
                "error": "Forbidden",
                "statusCode": 403,
                "correlationId": "zxeujsqc",
            }
        ),
    },
    "albums/NOTFOUND?withoutAssets=false": {
        "status": 404,
        "body": json.dumps(
            {
                "message": "Cannot GET /api/server/version-check",
                "error": "Not Found",
                "statusCode": 404,
                "correlationId": "4l3qxp07",
            }
        ),
    },
    "albums/CLIENT_ERROR?withoutAssets=false": {
        "status": None,
        "body": None,
        "exception": ClientError,
    },
}
