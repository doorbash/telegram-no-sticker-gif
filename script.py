from telethon import TelegramClient, events, sync
from telethon.types import PeerUser, MessageMediaContact
import logging, os, socks, dbm

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',level=logging.WARNING)

documents = dbm.open('db/documents', 'c')
users = dbm.open('db/users', 'c')

if os.environ.get('PROXY'):
    host = os.environ['PROXY_IP']
    port = int(os.environ['PROXY_PORT'])
    proxy = (socks.SOCKS5, host, port)
else:
    proxy = None

client = TelegramClient('default', os.environ['API_ID'], os.environ['API_HASH'], proxy=proxy)
client.start()

@client.on(events.NewMessage)
async def my_event_handler(event):
    if type(event.message.peer_id) != PeerUser: return

    is_from_myself = event.message.peer_id.user_id == me.id 

    if is_from_myself and event.message.out and type(event.message.media) == MessageMediaContact:
        user_id = str(event.message.media.user_id)
        if users.get(user_id):
            del users[user_id]
            await event.reply('removed from `no sticker/gif - users` list! send again to add it')
        else:
            users[user_id] = "."
            await event.reply('added to `no sticker/gif - users` list! send again to remove it')
        return

    is_media = event.message.media != None and event.message.document != None 
    is_sticker = is_media and event.message.document.mime_type in ("image/webp", "application/x-tgsticker", 'video/webm')
    is_gif = is_media and event.message.document.mime_type in ("video/mp4") and event.message.document.size < 1024 * 1024
    
    if is_sticker or is_gif:
        document_id = str(event.message.media.document.id)
        if is_from_myself:
            if documents.get(document_id):
                del documents[document_id]
                await event.reply('removed from `no sticker/gif - documents` list! send again to add it')
            else:
                documents[document_id] = "."
                await event.reply('added to `no sticker/gif - documents` list! send again to remove it')
        else:
            user_id = str(event.message.peer_id.user_id)
            if documents.get(document_id) or users.get(user_id):
                await event.delete()
        
me = client.get_me()
print(me.stringify())
	
with client:
    client.run_until_disconnected()