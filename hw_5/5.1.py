import os

import asyncio
import aiohttp
import aiofiles

from typing import Any

async def download_and_save_file(url: str, filename: str, session: Any) -> None:
    response = await session.get(url)
    data = await response.read()
    async with aiofiles.open(filename, "wb") as f:
        await f.write(data)


async def main(url: str, save_path: str, img_num: int) -> None:
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *(
                download_and_save_file(
                    url, os.path.join(save_path, f"{i}.png"), session
                )
                for i in range(img_num)
            )
        )


if __name__ == "__main__":
    url = "https://picsum.photos/200"
    artifacts_dir = os.path.join(os.getcwd(), "hw_5", "artifacts", "5.1")
    asyncio.run(main(url, artifacts_dir, 100))
