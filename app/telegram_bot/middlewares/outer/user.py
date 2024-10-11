from typing import Any, Awaitable, Callable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram.types import User as AiogramUser

from app.services.database.repositories.general import GeneralRepository
from app.services.database.uow import UoW


class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any | None:
        aiogram_user: AiogramUser | None = data.get('event_from_user')
        if aiogram_user is None or aiogram_user.is_bot:
            return await handler(event, data)

        repository: GeneralRepository = data['repository']
        uow: UoW = data['uow']

        data['user'] = self._get_or_create(aiogram_user, repository, uow)
        return await handler(event, data)

    @staticmethod
    async def _get_or_create(
        aiogram_user: AiogramUser,
        repository: GeneralRepository,
        uow: UoW,
    ) -> User:
        user: User | None = await repository.users.get_by_id(telegram_id=aiogram_user.id)
        if user is None:
            user = await repository.users.create(aiogram_user=aiogram_user, uow=uow)
        return user
