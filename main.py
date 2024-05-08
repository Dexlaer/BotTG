import asyncio  # Импорт асинхронного ввода/вывода
import config  # Импорт файла конфигурации, где обычно хранится токен бота
from aiogram import Bot, Dispatcher, types, F  # Импорт основных классов из aiogram
from aiogram.filters.command import Command  # Импорт фильтра команд из aiogram
import logging  # Импорт модуля логирования
import random  # Импорт модуля random для генерации случайных чисел
from keybords import keyboard
####################
import requests


def fox():
    url = 'https://randomfox.ca/floof/'
    response = requests.get(url)
    if response.status_code:
        data = response.json()
        image = data.get('image')
        return image

    if __name__ == '__main__':
        print(fox())

################
logging.basicConfig(level=logging.INFO)  # Настройка логирования для отображения информационных сообщений
#
# # Создание объекта бота и диспетчера для обработки сообщений
bot = Bot(token=config.token)  # Создаем экземпляр бота с токеном из файла config
dp = Dispatcher()  # Создаем экземпляр диспетчера

# Список комплиментов
compliments = [
    "Ты свет моей жизни!",
    "Ты самая замечательная!",
    "Твоя улыбка освещает мой день!",
    "Я так счастлив, что ты со мной!",
    "Ты вдохновляешь меня каждый день!"
]

# Список цитат
quotes = [
    "Любовь – это когда два сердца бьются в унисон.",
    "Счастье – это момент, проведенный с любимыми.",
    "Жизнь – это путешествие, на котором лучше быть вдвоем.",
    "Лучший способ быть счастливым – делить счастье с другими.",
    "Любовь делает все возможным."
]

@dp.message(Command(commands=['start']))
async def send_welcome(message: types.Message):
    await message.answer(f'Привет! Чем я могу тебя порадовать сегодня? Напиши /compliment или /quote 🌹', reply_markup=keyboard)

@dp.message(Command(commands=['compliment']))
async def send_compliment(message: types.Message):
    compliment = random.choice(compliments)
    await message.answer(compliment)

@dp.message(Command(commands=['quote']))
async def send_quote(message: types.Message):
    quote = random.choice(quotes)
    await message.answer(quote)

@dp.message(Command(commands=['stop']))
async def send_goodbye(message: types.Message):
    await message.answer(f'Пока! Всегда рад тебя видеть 💖')

@dp.message(F.text.lower() == 'число')
async def info(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Привет, твоё число: {number}!')

@dp.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')

@dp.message(F.text.lower() == 'лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Нет, не покажу')
    await message.answer_photo(img_fox)
    img_fox = fox()
    await bot.send_photo(message.from_user.id, img_fox)

# async def main():
#     await dp.start_polling()
#
# if __name__ == "__main__":
#     asyncio.run(main())

async def main():  # Главная асинхронная функция
    await dp.start_polling(bot)  # Запуск бота на опрос сообщений

if __name__ == "__main__":  # Если файл запущен как основной, а не импортирован
    asyncio.run(main())  # Запускаем асинхронный цикл




