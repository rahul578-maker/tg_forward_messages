from telethon import TelegramClient, events
import time
import asyncio


# create your id and hash here: https://my.telegram.org/auth
api_id = 626980225
api_hash = 'AAGrK9eQmT4-Ay8b4Qv_NN9MtG7_KRjlYy0'

# ID of private group in telegram, find out here: @username_to_id_bot
chats_id = [-1798894870, -1798894870]
# ID of your channel, find out here: @Xx12Xx_Bot
my_channel_id = -1904619787

# Topic ID from 1st group
topic_id_1 = 1000
# Topic ID from 2nd group
topic_id_2 = 1000

client = TelegramClient('python_bot', api_id, api_hash)
client.start(password=input('Enter your 2FA password: 1 '))

@client.on(events.NewMessage(chats=chats_id))
async def main(event):

    if event.reply_to != None:
        if event.reply_to.reply_to_msg_id == topic_id_1:
            await client.forward_messages(my_channel_id, event.message)
        if event.reply_to.reply_to_msg_id == topic_id_2:
            await client.forward_messages(my_channel_id, event.message)

client.run_until_disconnected()
