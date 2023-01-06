import httpx
from nonebot import logger
import asyncio

async def get_url() -> str:
    """
    :return: 早报图片链接
    """
    url="https://www.loliapi.com/acg/pc/?type=json"
    async with httpx.AsyncClient() as client:
        r = (await client.get(url=url))
        r = r[r.text.find('https'),r.text.find('.jpg')+4]
        return r
if __name__ == '__main__':
    asyncio.run(get_url())