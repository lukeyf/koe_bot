import json
import os
from pathlib import Path

from nonebot import on_command,on_message
import nonebot
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, MessageEvent, MessageSegment
import random
global_config = nonebot.get_driver().config
matcher = on_message(to_me(), priority=4, block=False)
bang_json = os.path.join(os.path.dirname(__file__),'resources','bang.json')
bang_jpg = os.path.join(os.path.dirname(__file__),'resources','bang.jpg')
banged_jpg = os.path.join(os.path.dirname(__file__),'resources','banged.jpg')
with open(bang_json) as json_file:
    BANGS = dict(json.load(json_file))
MessageSegment.image(bang_jpg)
@matcher.handle()
async def handle_func(event: MessageEvent):
    # do something here
    msg = str(event.get_message())

    if msg[0] == '梆':
        try:
            assert msg.find(']') > 1
            bangee = msg[msg.find('qq=')+3:msg.find(']')]
            if bangee in BANGS.keys():
                await matcher.send(message=MessageSegment.at(str(event.get_user_id()))+
                                   MessageSegment.text(random.choice(BANGS[bangee])))
            else:
                await matcher.send(message=MessageSegment.at(bangee) +
                                           MessageSegment.image(Path(bang_jpg)))
        except:
            await matcher.send(message=MessageSegment.at(str(event.get_user_id()))+
                                       MessageSegment.image(Path(banged_jpg))
                               )

        matcher.stop_propagation(matcher)

