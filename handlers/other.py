from aiogram import types, Dispatcher
import json, string
from create_bot import dp

# @dp.message_handler()
async def echo_send(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('danger.json')))) != set():
        await message.reply('Маты запрещены')
        await message.delete()

def register_hadlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)

    # if message.text == 'Привет':
    #     await message.answer('Здравствуйте')
    # await message.answer(message.text)
    #  await message.reply(message.text)
    #  await bot.send_message(message.from_user.id, message.text)



