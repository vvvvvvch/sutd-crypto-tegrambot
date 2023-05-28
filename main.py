import requests
import logging
import config
from aiogram import Bot, Dispatcher, types
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

# Initialize bot keyboard
currency_kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
currency_kb.row(*[types.KeyboardButton(x) for x in config.TOP_CURRENCIES_LIST])

exchange_kb = types.InlineKeyboardMarkup().add(
    types.InlineKeyboardButton('USD', callback_data='exchange_button_usd'),
    types.InlineKeyboardButton('RUB', callback_data='exchange_button_rub'),
    types.InlineKeyboardButton('EUR', callback_data='exchange_button_eur')
)


# Set exchange callback
@dp.callback_query_handler(lambda c: c.data and c.data.startswith('exchange_button'))
async def set_exchange(callback_query: types.CallbackQuery):
    code = callback_query.data[-3:]
    config.LOCAL_STORAGE[callback_query.from_user.id] = code.upper()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        f'Валюта для обмена: {config.LOCAL_STORAGE[callback_query.from_user.id]}'
    )


# Get currency rate
def get_rate(currency: str, exchange: str):
    headers = {'X-CoinAPI-Key': config.API_KEY, 'Content-Type': 'application/json'}
    response = requests.get(config.ENDPOINT + f'/exchangerate/{currency}/{exchange}', headers=headers)
    return response.json()["rate"]


# Get assets list
def get_assets():
    headers = {'X-CoinAPI-Key': config.API_KEY, 'Content-Type': 'application/json'}
    response = requests.get(config.ENDPOINT + f'/assets', headers=headers)
    return [x['asset_id'] for x in response.json()]


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    exchange = config.LOCAL_STORAGE[
        message.from_user.id] if message.from_user.id in config.LOCAL_STORAGE else config.DEFAULT_EXCHANGE
    await message.reply(f"Привет!\n"
                        f"Я конвертер криптовалют\n"
                        f"Мне известно: {len(config.CURRENCIES_LIST)} криптовалют\n"
                        f"\n"
                        f"Текущая валюта: {exchange}\n"
                        f"Для смены используйте команду /exchange\n"
                        f"Введите криптовалюту, которую хотите конвертировать", reply_markup=currency_kb)


@dp.message_handler(commands=['exchange'])
async def get_exchange(message: types.Message):
    await message.reply(f"Выберете валюту:", reply_markup=exchange_kb, reply=False)


@dp.message_handler()
async def echo(message: types.Message):
    input_currency = message.text.upper()
    logging.info(f"Input message: {input_currency}")
    if input_currency not in config.CURRENCIES_LIST:
        answer = f"Извините, я не знаю такой валюты. Попробуйте другую валюту"
    else:
        exchange = config.LOCAL_STORAGE[
            message.from_user.id] if message.from_user.id in config.LOCAL_STORAGE else config.DEFAULT_EXCHANGE
        answer = f"В одном {input_currency} - {get_rate(input_currency, exchange)} {exchange}"
    await message.answer(answer)


async def main():
    config.CURRENCIES_LIST = get_assets()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
