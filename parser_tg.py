import configparser
import json

from telethon import TelegramClient, sync, events
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, time

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest

import time

api_id = 28362818
api_hash = 'e2ddf5c57f4a4ff520fe4c4335851152'
username = 'Maksim_Kub'
my_id = 745497120
channel_id = 1001199360700

client = TelegramClient(username, api_id, api_hash)
client.start()

async def main():
    async with client:

        async for massege in client.iter_messages(channel_id,limit=30):
            i = []
            i.append(massege.text)
            print(i)

with client:
    client.loop.run_until_complete(main())


# masege = client.get_messages(channel_id)
# for a in masege:
#     print(a.text)

# поиск id
# dialogs = client.get_dialogs()
# for dialog in dialogs:
#     if dialog.title == 'Труха⚡️Украина':
#         print("ID чата ", dialog.id )



import sqlite3

con = sqlite3.connect('order.bd')
cur = con.cursor()

con.execute('''CREATE TABLE IF NOT EXISTS users( 
userid INT PRIMARY KEY,
fname TEXT,
lname TEXT,
gender TEXT
);

''')
con.commit()

user = ('00002', 'Lois', 'Lane', 'Female')

con.execute('INSERT INTO users VALUES(?,?,?,?);', user)
