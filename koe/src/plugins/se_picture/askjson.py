import httpx
from nonebot import logger


async def get_url() -> dict:
    """
    :return: 早报图片链接
    """
    url="https://www.loliapi.com/bg/"
    async with httpx.AsyncClient() as client:
        r = (await client.get(url=url)).json()
        return r