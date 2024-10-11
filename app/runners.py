from aiogram import Bot, Dispatcher


def run_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    return dispatcher.run_polling(bot)
