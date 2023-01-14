
"https://github.com/aiogram/aiogram/blob/dev-2.x/examples/inline_keyboard_example.py"

import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


def create_i_key():
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    text_and_data = (
        ('Drake', 'Drake'),
        ('21 savage', '21 savage'),
        ('Trippie Redd', 'Trippie Redd')
    )
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard.row(*row_btns)
    keyboard.add(
        # url buttons have no callback data
        types.InlineKeyboardButton('aiogram source', url='https://github.com/aiogram/aiogram'),
    )
    return keyboard


@dp.message_handler(commands='ikeyb')
async def start_cmd_handler(message: types.Message):
    await message.reply("Hi!\nDo you love aiogram?", reply_markup=create_i_key())


# Use multiple registrators. Handler will execute when one of the filters is OK
@dp.callback_query_handler(text='no')  # if cb.data == 'no'
@dp.callback_query_handler(text='yes')  # if cb.data == 'yes'
async def inline_kb_answer_callback_handler(query: types.CallbackQuery):
    answer_data = query.data
    # always answer callback queries, even if you have nothing to say
    await query.answer(f'You answered with {answer_data!r}')

    if answer_data == 'yes':
        text = 'Great, me too!'
    elif answer_data == 'no':
        text = 'Oh no...Why so?'
    else:
        text = f'Unexpected callback data {answer_data!r}!'

    await bot.send_message(query.from_user.id, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)