from aiogram import Bot, Dispatcher, types, executor
import random

bot = Bot("6055189563:AAG4NqnS1UPra6nL_T3-H2XrPZ0FTq2ghmo")
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.answer("Привет!")
    await message.answer("Я загадал число от 1 до 3, отгадай: ")


@dp.message_handler(text=['1', '2', '3'])
async def play(message:types.Message):
    secret_number = random.randint(1, 3)
    if int(message.text) == secret_number:
        await message.reply('Правильно, вы отгадали!')
    else:
        await message.reply(f'Неправильно. Я загадал число {secret_number}.')


executor.start_polling(dp)