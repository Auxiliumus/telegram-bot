from sqlalchemy.ext.asyncio import AsyncSession


class _BaseRepository:
    _session: AsyncSession

    def __init__(self, session: AsyncSession) -> None:
        self._session = session


class GeneralRepository(_BaseRepository):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session=session)
