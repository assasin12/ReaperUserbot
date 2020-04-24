"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio
from uniborg.util import admin_cmd
from telethon.tl.functions.users import GetFullUserRequest



@borg.on(admin_cmd(pattern=r"hack"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "hack":

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        if idd==1076931233:
            await event.edit("This is My Master\nI can't hack my master's Account\n**How dare you trying to hack my master's account nigger!**\n\n__Your account has been hacked! Pay 69$ to my master__ [ɢʀɨʍ ЯΣΛPΣЯ](tg://user?id=1076931233) __to release your account__😏")
        else:
            await event.edit("Hacking..")
            animation_chars = [
        
            "`Connecting To Hacked Private Server...`",
            "`Target Selected.`",
            "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Hacking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 84%\n█████████████████████▒▒▒▒ `",
            "`Hacking... 100%\n█████████HACKED███████████ `",
            "`Wew! My peruu master has hacked your account successfully...\n\nPay 69k $ To` @GrimReapeer `To Remove this hack or your all data will be leaked`"
            ]

            for i in animation_ttl:

                await asyncio.sleep(animation_interval)

                await event.edit(animation_chars[i % 11])
    else:
        await event.edit("No User is Defined\n Can't hack account")
