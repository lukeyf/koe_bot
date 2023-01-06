import nonebot
from nonebot import on_command,logger
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
from . import askjson
import random
REPLY = [
        "没有，有也不给",
        "天天色图色图的，今天就把你变成色图！",
        "咱没有色图",
        "哈？你的脑子一天都在想些什么呢，咱才没有这种东西啦。"
    ]
se_pic=on_command("色图",aliases={"涩图"},priority=2,block=True)
@se_pic.handle()
async def _(bot:Bot,event:MessageEvent):
    if random.random()>0.3:
        img_url=(await askjson.get_url())
        if img_url:
            await se_pic.send(message=MessageSegment.image(img_url))
        else:
            logger.info('获取时出现错误')
    else:
        r = random.choice(REPLY)
        await se_pic.send(message=r)
