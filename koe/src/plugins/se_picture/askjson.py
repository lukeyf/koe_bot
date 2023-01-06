import httpx
from nonebot import logger
import asyncio

async def get_url() -> dict:
    """
    :return: 早报图片链接
    """
    url="https://api.1314.cool/img/sort/api/api.php?return=json"
    async with httpx.AsyncClient() as client:
        r = (await client.get(url=url)).json()
        return r
