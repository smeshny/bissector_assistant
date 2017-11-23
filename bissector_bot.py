from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram import types


from config import token
from ethermine_check import check_status_ethermine
from etherscan_check import ether_scan


bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
        await message.reply("Привет! \nЯ ассистент чата Биссектора. "
                            "\nПока что. \nСкоро стану скайнетом")


@dp.message_handler(commands=['menu'])
async def add_menu(message: types.Message):

        miners = types.KeyboardButton("/miners")
        balance = types.KeyboardButton("/balance")
        markup = types.ReplyKeyboardMarkup([[miners, balance]], True, False)

        await bot.send_message(chat_id=message.chat.id, text="Жми!", reply_markup=markup)

@dp.message_handler(commands=['miners'])
async def check_miners(message: types.Message):
        await bot.send_message(chat_id=message.chat.id, text=check_status_ethermine(), parse_mode='Markdown')


@dp.message_handler(commands=['balance'])
async def check_eth_balance(message: types.Message):
        await bot.send_message(chat_id=message.chat.id, text=ether_scan(), parse_mode='Markdown')


if __name__ == '__main__':
        executor.start_pooling(dp)


'''
commands:
menu - вызвать меню
balance - узнать количество эфира на кошельке
miners - узнать статистику по ферме
'''