from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import types


from config import token


bot = Bot(token=token)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
        await message.reply("Привет! \nЯ ассистент чата Биссектора. "
                            "\nПока что. \nСкоро стану скайнетом")

@dp.message_handler(commands=['miners'])
async def check_miners(message: types.Message):
        await bot.send_message(chat_id=message.chat.id, text="тут будет статистика ригов")


@dp.message_handler(commands=['balance'])
async def check_eth_balance(message: types.Message):
        await bot.send_message(chat_id=message.chat.id, text="тут бусдет статистика кошелька")


if __name__ == '__main__':
        executor.start_pooling(dp)
