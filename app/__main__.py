from aiogram import Bot, Dispatcher

from .app_config import AppConfig
from .factories import create_app_config, create_bot, create_dispatcher
from .runners import run_polling
from .utils.loggers import setup_logger


def main() -> None:
    setup_logger()
    config: AppConfig = create_app_config()
    dispatcher: Dispatcher = create_dispatcher(config=config)
    bot: Bot = create_bot(config=config)
    # if config.telegram.use_webhook:
    #     return run_webhook(dispatcher=dispatcher, bot=bot, config=config)
    return run_polling(dispatcher=dispatcher, bot=bot)


if __name__ == "__main__":
    main()
