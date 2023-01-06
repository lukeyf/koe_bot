import nonebot
from nonebot import on_command,logger
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
from . import askjson
import random

se_pic=on_command("来一份色图",aliases={"来一份涩图"},priority=2,block=True)
@se_pic.handle()
async def _(bot:Bot,event:MessageEvent):
    if random.random()>0.2:
        img_url=(await askjson.get_url())
        if img_url:
            await se_pic.send(message=MessageSegment.image(img_url["imgurl"]))
        else:
            logger.info('获取时出现错误')
    else:
        await se_pic.send(message='不行，不可以涩涩')