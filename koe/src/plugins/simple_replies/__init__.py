from nonebot import on_command,logger
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
import random

se_pic=on_command("来一份色图",aliases={"来一份涩图"},priority=6,block=True)
@se_pic.handle()
async def _(bot:Bot,event:MessageEvent):
    pass