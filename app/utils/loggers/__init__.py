import logging

from .multiline import MultilineLogger
from .setup import disable_aiogram_logs, setup_logger

database: logging.Logger = logging.getLogger('bot.database')
middleware: logging.Logger = logging.getLogger('bot.middleware')
