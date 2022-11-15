import datetime

import requests
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import token


bot = Bot('Your telegram bot token')
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Привет! Напиши название города")


@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token}&units=metric")
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        print('*********************')
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])
        await message.reply(f"___ {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')} ___\n"
                            f"Погода в городе: {city}\n"
                            f"Температура: {cur_weather}°C\n"
                            f"Влажность воздуха: {humidity}%\n"
                            f"Скорость ветра: {wind} m/c\n"
                            f"Восход солнца: {sunrise}\n"
                            f"Заход солнца: {sunset}\n"
                            f"Продолжительность дня: {length_of_day}\n"
                            f"Хорошего дня!")

    except:
        await message.reply("Проверьте название города!")


if __name__ == '__main__':
    executor.start_polling(dp)

