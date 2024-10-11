from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from redis.asyncio import Redis

from .redis import create_redis
from .session_pool import create_session_pool
from app.telegram_bot.middlewares.outer.database import DBSessionMiddleware
from app.telegram_bot.middlewares.outer.user import UserMiddleware
from app.utils import msgspec_json as mjson
from app.app_config import AppConfig


def create_dispatcher(config: AppConfig) -> Dispatcher:
    redis: Redis = create_redis(url=config.redis.build_url())

    dispatcher: Dispatcher = Dispatcher(
        name='main_dispatcher',
        storage=RedisStorage(
            redis=redis,
            json_loads=mjson.decode,
            json_dumps=mjson.encode,
        ),
        config=config,
        session_pool=create_session_pool(url=config.postgres.build_url()),
        # redis=RedisRepository(client=redis),
    )

    # dispatcher.include_routers(admin.router, common.router, extra.router)
    dispatcher.update.outer_middleware(DBSessionMiddleware())
    dispatcher.update.outer_middleware(UserMiddleware())
    dispatcher.callback_query.middleware(CallbackAnswerMiddleware())

    return dispatcher
