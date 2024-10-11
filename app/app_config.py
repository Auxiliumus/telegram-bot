from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings as _BaseSettings
from pydantic_settings import SettingsConfigDict
from sqlalchemy import URL


class BaseSettings(_BaseSettings):
    model_config = SettingsConfigDict(
        extra='ignore',
        env_file='.env',
        env_file_encoding='utf-8',
    )


class BotConfig(BaseSettings, env_prefix='BOT_'):
    token: SecretStr
    admin_id: int


class PostgresConfig(BaseSettings, env_prefix='POSTGRES_'):
    host: str
    user: str
    password: SecretStr
    db: str
    port: int

    def build_dsn(self) -> URL:
        return URL.create(
            drivername='postgresql+asyncpg',
            username=self.user,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.db,
        )


class RedisConfig(BaseSettings, env_prefix='REDIS_'):
    host: str
    db: int
    port: int


class MinioConfig(BaseSettings, env_prefix='MINIO_'):
    host: str
    user: str
    password: SecretStr
    bucket_name: str
    port: int
    use_ssl: bool


class AppConfig(BaseModel):
    bot: BotConfig
    postgres: PostgresConfig
    redis: RedisConfig
    minio: MinioConfig
