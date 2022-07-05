from aiogram.utils import executor
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
import os


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await message.reply('Здоров')


#отражает команду
@dp.message_handler(commands=['команда'])
async def echo(message : types.Message):
    await message.answer(message.text)


# проверяет значение в строке
@dp.message_handler(lambda message: 'авто' in message.text)
async def taxi(message: types.Message):
    await message.answer('авто')


# проверяет значение в строке
@dp.message_handler(lambda message: message.text.startswith('такси'))
async def taxi(message: types.Message):
    await message.answer(message.text[6:])




async def echo(message : types.Message):
    await message.answer(message.text)

#пустой хендлер в который попадает всё остальное
@dp.message_handler()
async def empty(message : types.Message):
    await message.answer('Нет такой команды')
    await message.delete()

executor.start_polling(dp, skip_updates=True)