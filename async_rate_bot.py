from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from test import get_data

currency = get_data()
print(len(currency))

bot = Bot(token='Your telegram bot token')
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен')


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Средний курс в Бишкеке"),
            types.KeyboardButton(text="Лучший курс в Бишкеке"),
            types.KeyboardButton(text="Курс НБКР")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите вариант"
    )
    await message.answer("Какой вид курса выберите?", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Средний курс в Бишкеке")
async def with_puree(message: types.Message):
    await message.reply(f"за последние два часа\n\n"
                        f"Валюта   |Покупка:      |Продажа:\n\n"
                        f"USD          {currency[0]}               {currency[1]}\n"
                        f"EUR          {currency[3]}               {currency[4]}\n"
                        f"RUB          {currency[5]}               {currency[6]}\n"
                        f"KZT          {currency[7]}             {currency[8]}\n"
                        f"CNY          {currency[9]}               {currency[10]}\n"
                        f"GBP          {currency[11]}             {currency[12]}")


@dp.message_handler(lambda message: message.text == "Лучший курс в Бишкеке")
async def without_puree(message: types.Message):
    await message.reply(f"Валюта   |Покупка:      |Продажа:\n\n"
                        f"USD          {currency[13]}               {currency[14]}\n"
                        f"EUR          {currency[15]}               {currency[16]}\n"
                        f"RUB          {currency[17]}               {currency[18]}\n"
                        f"KZT          {currency[19]}             {currency[20]}\n"
                        f"CNY          {currency[21]}               {currency[22]}\n"
                        f"GBP          {currency[23]}             {currency[24]}")


@dp.message_handler(lambda message: message.text == "Курс НБКР")
async def without_puree(message: types.Message):
    await message.reply(f"Валюта   |Продажа:\n\n"
                        f"USD          {currency[25]}\n"
                        f"EUR          {currency[26]}\n"
                        f"RUB          {currency[27]}\n"
                        f"KZT          {currency[28]}\n"
                        f"CNY          {currency[29]}\n"
                        f"GBP          {currency[-1]}")


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)

## ikb = InlineKeyboardMarkup(row_width=2)
# ib1 = InlineKeyboardButton(text="YouTube", callback_data='привет')
# ib2 = InlineKeyboardButton(text='Google', url='google.com')
#
# ikb.add(ib1)
# ikb.add(ib2)
#
# kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# b = KeyboardButton(text='/links')
#
# kb.add(b)


# @dp.message_handler(commands=['start'])
# async def start_command(message: types.Message):
#     await message.answer(text='Главное меню', reply_markup=kb)
#
#
# @dp.message_handler(commands=['links'])
# async def links_command(message: types.Message):
#     await message.answer(text='Выберите опцию', reply_markup=ikb)


# @dp.message_handler(commands=['rate'])
# async def get_rate(message: types.Message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton('Средний курс в Бишкеке')
#     item2 = types.KeyboardButton('Лучший курс в Бишкеке')
#     item3 = types.KeyboardButton('Курс НБКР')
#     markup.row(item1, item2, item3)
#
#     await message.reply(reply_markup=markup)
#
#
# # @dp.message_handler(content_types=['text'])
# # async def get_rate(message: types.Message)
#
