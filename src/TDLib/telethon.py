import builtins,time
from telethon import TelegramClient, events, sync,functions,errors
from telethon.tl.custom import button
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputPeerChat

class TELETHON:
    def __init__(self):
        api_id = 10154258
        api_hash = "15ae4e0dbe1c43d14b6e094f07420afb"
        self.client = TelegramClient('leo',api_id = api_id, api_hash = api_hash)
        
    async def send_message_to_group(self,chat_id, message):
        chat = await self.client.get_entity(chat_id)
        await self.client.send_message(chat, message)
        
    async def send_message_to_user(self,chat_id, message):
        chat = InputPeerChat(chat_id)
        await self.client.send_message(chat, message)
        
    async def main(self):
        async with self.client:
            # print(await self.client.get_entity("hank6515000"))
            entity = await self.client.get_entity(6056596947)
            await self.client.send_message(entity,"1")
            # await self.client.start()
            # await self.send_message_to_user(-1001885441881, "1")
            # await self.client.run_until_disconnected()
        
def run():
    telethon = TELETHON()
    telethon.client.loop.run_until_complete(telethon.main())
