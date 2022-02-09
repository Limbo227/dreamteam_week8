import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from pprint import pprint as pp
import json


tg_bot_token  = '5053091247:AAHUXGjf2rq9aJhl_P4u_QcoRkfmTehOySg'
bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

# with open ('bak.json', 'a') as file:
#     for i in range(5):
#         evil = requests.get(url=f'https://kitsu.io/api/edge/anime?filter[text]=tokio%2F1&page[limit]=20&page[offset]={i}')
#         data = evil.json()
#         anime = data['data']
#         json.dump(anime, file)
# with open('bak.json', 'r') as f:
#     anime2 = json.load(f)
evil = requests.get(url=f'https://kitsu.io/api/edge/anime?filter[text]=tokio%2F1&page[limit]=20&page[offset]=1-5')
data = evil.json()
anime = data['data']
animeshki = dict()

for values in anime:
    animeshki[values['attributes']['canonicalTitle']] = values



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Называние anime! ")

@dp.message_handler()
async def get_info_about_anime(message: types.Message):
    searched = animeshki.get(message.text)
    if searched is None:
        await message.reply("sorry not find")
    await message.reply(f"""
    Title : {searched['attributes']['canonicalTitle']}
    Type : {searched['type']}
    Description : {searched['attributes']['description']}
    {searched['attributes']['posterImage']['original']}
    """)


executor.start_polling(dp)
