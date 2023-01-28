import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

commands = (
    ('help', 'список доступных команд'),
    ('com1', 'это команда 1')
)


@dp.message_handler(commands='help')
def info_giving(message):
    #for c in commands:
       # if commands[c] in
    text = f"Ваши доступные команды:\n{commands}"
    message.reply(text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)