from telethon import events
from __main__ import client
import time
from constants import Config

CMD_PREFIX  = Config.CMD_PREFIX

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "hexa (.*) (\w+)"))
async def help(event):
    bid = 572621020
    msg = "/hunt"
    times_hunt = event.pattern_match.group(1)
    set_sec = event.pattern_match.group(2)
    eta = int((int(times_hunt) * int(set_sec))/60)
    if not times_hunt.isnumeric():
        text = "`Onii-sama nHunts and nSex both must be integers :)`"
        await event.edit(text)
    else:
        await event.edit("`Aye aye Captain... `"
                        "\n`Started hunting right away on yer command 🤠`"
                        f"\n\n`Will be hunting {times_hunt} times. Each one of 'em in {set_sec} seconds.`"
                        f"\n\n`ETA for this hunt is around: {eta} minutes.`")
        for i in range(int(times_hunt)):
            await client.send_message(bid,msg)
            if int(i) == int(times_hunt)-1:
                await event.reply("`Hunting complete.`")
            else:
                time.sleep(int(set_sec))